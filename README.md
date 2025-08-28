📝 TO-DO LIST WITH AI AGENT






🎯 PROJECT OVERVIEW

A powerful To-Do List Manager enhanced with an AI-powered agent that processes natural language commands via fallback pattern matching—no external AI API needed.

Built for Foyr AI Hackathon 2025, the app offers:

Manual Task Control via intuitive UI

Intelligent AI Control via natural language commands

✅ All actions are accessible in both modes, giving a seamless user experience.

✨ FEATURES
Feature	Description
✅ Task Management	Add, complete, delete, and list tasks manually or via AI commands
🤖 Simple AI Agent	Understands commands via regex-based natural language fallback
🔁 Conversation History	Tracks the latest 10 user-agent interactions
🎨 Dual-Mode Parity	Same functionalities accessible via UI or AI chat
🚀 Lightweight & Self-Hosted	No external AI API; runs fully with minimal dependencies
📦 TECH STACK

Backend: Python 3 + FastAPI

Frontend: Static index.html served via FastAPI

AI Agent Logic: Custom fallback pattern matching

Deployment: Hosted on Render

CORS: Enabled for cross-origin frontend-backend communication

🌐 LIVE DEMO

Try it here: Click to Open

💬 SUPPORTED COMMANDS

Add Task

add buy groceries
create task read book


Complete Task

mark task 2 done
complete task 1


Delete Completed Tasks

delete all done tasks


List Tasks

list my tasks
show tasks

🚀 SETUP & RUN LOCALLY
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload


Open your browser at http://localhost:8000
 to start using the app.
