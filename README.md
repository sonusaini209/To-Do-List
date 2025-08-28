**To-Do List with AI Agent**
Python| 💻 Repo

🎯 Project Overview
A to-do list manager enhanced with an AI-powered agent interface that processes natural language commands through fallback pattern matching—no external AI API needed.

Built for the Foyr AI Hackathon 2025, this app highlights a dual-mode interaction:

Manual task control via intuitive UI

Intelligent control via a natural language AI agent

All actions are fully accessible in both modes for seamless user experience.

✨ Features
Feature	Description
✅ Task Management	Add, complete, delete, and list tasks manually or via AI commands
🤖 Simple AI Agent	Understands commands via regex-based natural language fallback
🔁 Conversation History	Tracks latest 10 user-agent interactions
🎨 Dual-Mode Parity	Same functionalities accessible via UI or AI chat
🚀 Lightweight & Self-Hosted	No external AI API; runs fully with minimal dependencies
📦 Tech Stack
Backend: Python 3 + FastAPI

Frontend: Static index.html served by FastAPI root endpoint

AI Agent Logic: Custom fallback pattern matching

Deployment: Hosted on Render

CORS: Enabled for cross-origin frontend-backend communication

🛠 Usage
Live Demo
Try the app here: https://to-do-list-7e75.onrender.com/

Commands Supported
Add task:

"add buy groceries"

"create task read book"

Complete task:

"mark task 2 done"

"complete task 1"

Delete completed tasks:

"delete all done tasks"

List tasks:

"list my tasks"

"show tasks"

🚀 Setup & Run Locally
bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Open browser at http://localhost:8000 to start using the app.
