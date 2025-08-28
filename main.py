from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import re, os
from typing import Optional, List
from datetime import datetime

app = FastAPI()

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

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

class AgentRequest(BaseModel):
    message: str

class AgentResponse(BaseModel):
    response: str
    action: Optional[str] = None
    task_id: Optional[int] = None

@app.get("/")
def read_root():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(current_dir, "index.html")
    return FileResponse(index_path)

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def add_task(title: str):
    global task_id
    task_id += 1
    task = Task(id=task_id, title=title, done=False)
    tasks.append(task.dict())
    return task

@app.patch("/tasks/{task_id}", response_model=Task)
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
    """AI agent endpoint using fallback pattern matching"""
    global conversation_history

    # Append user message
    conversation_history.append({"role": "user", "message": request.message, "timestamp": datetime.now().isoformat()})

    # Process message
    result = fallback_pattern_matching(request.message)

    # Append agent response
    conversation_history.append({"role": "assistant", "message": result["response"], "timestamp": datetime.now().isoformat()})

    return AgentResponse(**result)

def fallback_pattern_matching(message: str) -> dict:
    global tasks, task_id
    msg = message.lower().strip()

    # Add task
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
        match = re.search(pattern, msg)
        if match:
            title = match.group(1).strip()
            task_id += 1
            task = {"id": task_id, "title": title, "done": False}
            tasks.append(task)
            return {
                "action": "ADD_TASK",
                "response": f"Added task: {title}",
                "task_id": task_id
            }

    # Complete task
    if "mark" in msg and ("done" in msg or "complete" in msg):
        task_match = re.search(r'task\s+(\d+)', msg)
        if task_match:
            tid = int(task_match.group(1))
            for task in tasks:
                if task["id"] == tid:
                    task["done"] = True
                    return {
                        "action": "COMPLETE_TASK",
                        "response": f"Marked task '{task['title']}' as completed",
                        "task_id": tid
                    }
        # No ID -> mark first incomplete
        for task in tasks:
            if not task["done"]:
                task["done"] = True
                return {
                    "action": "COMPLETE_TASK",
                    "response": f"Marked task '{task['title']}' as completed",
                    "task_id": task["id"]
                }

    # Delete completed tasks
    if ("delete" in msg or "remove" in msg) and ("all" in msg and "done" in msg):
        deleted_count = len([t for t in tasks if t["done"]])
        tasks[:] = [t for t in tasks if not t["done"]]
        return {
            "action": "CLEAR_COMPLETED",
            "response": f"Deleted {deleted_count} completed tasks"
        }

    # List tasks
    if any(word in msg for word in ["list", "show", "what"]):
        if not tasks:
            return {"action": "LIST_TASKS", "response": "You have no tasks yet!"}
        task_list = [f"{'[done]' if t['done'] else '[pending]'} {t['id']}: {t['title']}" for t in tasks]
        return {
            "action": "LIST_TASKS",
            "response": "Your tasks:\n" + "\n".join(task_list)
        }

    # Fallback
    return {
        "action": "CLARIFY",
        "response": "I didn't understand that. Try: 'add [task]', 'mark task done', 'list tasks', or 'delete completed'"
    }

@app.get("/conversation-history")
def get_conversation_history():
    """Get the last 10 conversation interactions"""
    return conversation_history[-10:]


