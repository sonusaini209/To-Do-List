from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import json
import re
from typing import Optional
from datetime import datetime

app = FastAPI()

# Mount static files to serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Allow frontend requests from any origin (adjust in production)
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
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    filtered_tasks = [t for t in tasks if t["id"] != task_id]
    if len(filtered_tasks) == len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[:] = filtered_tasks
    return {"message": "Deleted"}

@app.post("/agent", response_model=AgentResponse)
def process_agent_command(request: AgentRequest):
    """AI agent endpoint using only fallback pattern matching"""
    global tasks, task_id, conversation_history

    # Append user message to conversation history
    conversation_history.append({"role": "user", "message": request.message, "timestamp": datetime.now().isoformat()})

    # Process message using fallback pattern matching
    result = fallback_pattern_matching(request.message)

    # Append agent response to conversation history
    conversation_history.append({"role": "assistant", "message": result["response"], "timestamp": datetime.now().isoformat()})

    return AgentResponse(**result)

def fallback_pattern_matching(message: str) -> dict:
    global tasks, task_id

    message = message.lower().strip()

    # Patterns to recognize add task commands
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
                "response": f"✅ Added task: {title}",
                "task_id": task_id
            }

    # Complete task patterns
    if "mark" in message and ("done" in message or "complete" in message):
        task_match = re.search(r'task\s+(\d+)', message)
        if task_match:
            tid = int(task_match.group(1))
            for task in tasks:
                if task["id"] == tid:
                    task["done"] = True
                    return {
                        "action": "COMPLETE_TASK",
                        "parameters": {"task_id": tid},
                        "response": f"✅ Marked task '{task['title']}' as completed",
                        "task_id": tid
                    }
        # If no task number specified, mark first incomplete task
        for task in tasks:
            if not task["done"]:
                task["done"] = True
                return {
                    "action": "COMPLETE_TASK",
                    "parameters": {"task_id": task["id"]},
                    "response": f"✅ Marked task '{task['title']}' as completed",
                    "task_id": task["id"]
                }

    # Delete completed tasks
    if ("delete" in message or "remove" in message) and ("all" in message and "done" in message):
        deleted_count = len([t for t in tasks if t["done"]])
        tasks[:] = [t for t in tasks if not t["done"]]
        return {
            "action": "CLEAR_COMPLETED",
            "parameters": {},
            "response": f"🗑️ Deleted {deleted_count} completed tasks"
        }

    # List tasks
    if any(word in message for word in ["list", "show", "what"]):
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
            "response": "📝 Your tasks:\n" + "\n".join(task_list)
        }

    # If no command recognized
    return {
        "action": "CLARIFY",
        "parameters": {},
        "response": "🤔 I didn't understand that. Try: 'add [task]', 'mark task done', 'list tasks', or 'delete completed'"
    }


@app.get("/conversation-history")
def get_conversation_history():
    """Get the last 10 conversation interactions"""
    return conversation_history[-10:]

