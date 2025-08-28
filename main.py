from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import openai
import json
import re
from typing import List, Optional
from datetime import datetime
app = FastAPI()
# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")
# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
# In-memory task list and conversation history
tasks = []
task_id = 0
conversation_history = []
class AgentRequest(BaseModel):
    message: str

class AgentResponse(BaseModel):
    response: str
    action: Optional[str] = None
    task_id: Optional[int] = None
@app.get("/")
def read_root():
    return FileResponse('static/index.html')
@app.get("/tasks")
def get_tasks():
    return tasks
@app.post("/tasks")
def add_task(title: str):
    global task_id
    task_id += 1
    task = {"id": task_id, "title": title, "done": False}
    tasks.append(task)
    return task
@app.patch("/tasks/{task_id}")
def mark_done(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    return {"error": "Task not found"}
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": "Deleted"}
@app.post("/agent", response_model=AgentResponse)
def process_agent_command(request: AgentRequest):
    """Enhanced AI agent endpoint with OpenAI integration"""
    global tasks, task_id, conversation_history

    # Add to conversation history
    conversation_history.append({"role": "user", "message": request.message, "timestamp": datetime.now().isoformat()})

    # Get current tasks context
    tasks_context = json.dumps(tasks, indent=2) if tasks else "No tasks currently exist."

    # Enhanced system prompt for better AI understanding
    system_prompt = f"""You are an intelligent task manager agent. You can help users manage their to-do list through natural language.
Current tasks: {tasks_context}
Available actions:
1. ADD_TASK: Add a new task with given title
2. COMPLETE_TASK: Mark a task as done by ID or description
3. DELETE_TASK: Remove a task by ID or description  
4. LIST_TASKS: Show current tasks
5. CLEAR_COMPLETED: Remove all completed tasks
6. SEARCH_TASKS: Find tasks containing specific keywords
Respond with JSON in this format:
{{
    "action": "ACTION_TYPE",
    "parameters": {{"title": "task title", "task_id": 123, "query": "search term"}},
    "response": "Natural language response to user"
}}
If the user's request is unclear or you need more information, set action to "CLARIFY" and ask for clarification.
Examples:
- "add buy milk" → {{"action": "ADD_TASK", "parameters": {{"title": "buy milk"}}, "response": "Added task: buy milk"}}
- "mark the first task done" → {{"action": "COMPLETE_TASK", "parameters": {{"task_id": 1}}, "response": "Marked task as completed"}}
- "delete all grocery tasks" → {{"action": "SEARCH_DELETE", "parameters": {{"query": "grocery"}}, "response": "Deleted grocery-related tasks"}}
"""
    try:
        # Use OpenAI API (you'll need to set OPENAI_API_KEY in secrets)
        response = process_with_openai(system_prompt, request.message)

        # Execute the action
        result = execute_agent_action(response)

        # Add to conversation history
        conversation_history.append({"role": "assistant", "message": result["response"], "timestamp": datetime.now().isoformat()})

        return AgentResponse(**result)

    except Exception as e:
        # Fallback to pattern matching if OpenAI fails
        result = fallback_pattern_matching(request.message)
        return AgentResponse(**result)
def process_with_openai(system_prompt: str, user_message: str) -> dict:
    """Process user message with OpenAI API"""
    import os

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise Exception("OpenAI API key not configured")

    client = openai.OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        temperature=0.3,
        max_tokens=300
    )

    try:
        content = response.choices[0].message.content.strip()
        # Extract JSON from response
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "").strip()

        return json.loads(content)
    except json.JSONDecodeError:
        # If JSON parsing fails, return a clarification request
        return {
            "action": "CLARIFY",
            "parameters": {},
            "response": "I'm having trouble understanding your request. Could you please rephrase it?"
        }
def fallback_pattern_matching(message: str) -> dict:
    """Fallback pattern matching when OpenAI is not available"""
    global tasks, task_id

    message = message.lower().strip()

    # Add task patterns
    add_patterns = [
        r'^add\s+(.+)$',
        r'^create\s+task\s+(.+)$',
        r'^create\s+(.+)$',
        r'^new\s+task\s+(.+)$',
        r'^i\s+need\s+to\s+(.+)$',
        r'^remind\s+me\s+to\s+(.+)$',
        r'^todo\s+(.+)$'
    ]

    for pattern in add_patterns:
        match = re.search(pattern, message)
        if match:
            title = match.group(1).strip()
            task_id += 1
            task = {"id": task_id, "title": title, "done": False}
            tasks.append(task)
            return {
                "action": "ADD_TASK",
                "parameters": {"title": title},
                "response": f"✅ Added task: {title}"
            }

    # Complete task patterns
    if "mark" in message and ("done" in message or "complete" in message):
        # Try to find task by number or description
        task_match = re.search(r'task\s+(\d+)', message)
        if task_match:
            tid = int(task_match.group(1))
            for task in tasks:
                if task["id"] == tid:
                    task["done"] = True
                    return {
                        "action": "COMPLETE_TASK",
                        "parameters": {"task_id": tid},
                        "response": f"✅ Marked task '{task['title']}' as completed"
                    }

        # Mark first incomplete task
        for task in tasks:
            if not task["done"]:
                task["done"] = True
                return {
                    "action": "COMPLETE_TASK",
                    "parameters": {"task_id": task["id"]},
                    "response": f"✅ Marked task '{task['title']}' as completed"
                }

    # Delete patterns
    if "delete" in message or "remove" in message:
        if "all" in message and "done" in message:
            deleted_count = len([t for t in tasks if t["done"]])
            tasks[:] = [t for t in tasks if not t["done"]]
            return {
                "action": "CLEAR_COMPLETED",
                "parameters": {},
                "response": f"🗑️ Deleted {deleted_count} completed tasks"
            }

    # List tasks
    if "list" in message or "show" in message or "what" in message:
        if not tasks:
            return {
                "action": "LIST_TASKS",
                "parameters": {},
                "response": "📝 You have no tasks yet!"
            }

        task_list = []
        for task in tasks:
            status = "✅" if task["done"] else "📋"
            task_list.append(f"{status} {task['title']}")

        return {
            "action": "LIST_TASKS", 
            "parameters": {},
            "response": f"📝 Your tasks:\n" + "\n".join(task_list)
        }

    return {
        "action": "CLARIFY",
        "parameters": {},
        "response": "🤔 I didn't understand that. Try: 'add [task]', 'mark task done', 'list tasks', or 'delete completed'"
    }
def execute_agent_action(action_data: dict) -> dict:
    """Execute the action determined by the AI"""
    global tasks, task_id

    action = action_data.get("action", "")
    params = action_data.get("parameters", {})
    response = action_data.get("response", "Action completed")

    if action == "ADD_TASK":
        title = params.get("title", "")
        if title:
            task_id += 1
            task = {"id": task_id, "title": title, "done": False}
            tasks.append(task)
            return {"action": action, "task_id": task_id, "response": response}

    elif action == "COMPLETE_TASK":
        tid = params.get("task_id")
        if tid:
            for task in tasks:
                if task["id"] == tid:
                    task["done"] = True
                    return {"action": action, "task_id": tid, "response": response}

    elif action == "DELETE_TASK":
        tid = params.get("task_id")
        if tid:
            tasks = [t for t in tasks if t["id"] != tid]
            return {"action": action, "task_id": tid, "response": response}

    elif action == "CLEAR_COMPLETED":
        tasks = [t for t in tasks if not t["done"]]
        return {"action": action, "response": response}

    return {"action": action, "response": response}
@app.get("/conversation-history")
def get_conversation_history():
    """Get the conversation history for context"""
    return conversation_history[-10:]  # Return last 10 interactions

