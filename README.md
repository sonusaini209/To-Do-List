To-Do List with AI Agent — Foyr AI Hackathon 2025
Live Demo

Overview
This project is a to-do list manager enhanced with a lightweight AI agent interface that understands natural language commands via fallback pattern matching (rule-based) to manage tasks.

Built for the Foyr AI Hackathon 2025, the app demonstrates an agent-friendly, dual-mode interface where users can interact either:

Manually via the UI for adding, completing, and deleting tasks

Intelligently via natural language chat commands processed by the AI agent backend

Features
Task management: Add, complete, list, and clear tasks manually or via chat commands.

AI agent: Processes simple natural language commands using fallback regex (no external LLM needed).

Dual mode parity: All actions achievable manually or through agent commands.

Conversation tracking: Maintains last 10 chat interactions for context and continuity.

Lightweight & self-contained: No external AI API dependencies, suitable for local or cloud deployment.

Tech Stack
Backend: Python 3 + FastAPI

Frontend: Static index.html served by FastAPI root endpoint

AI Agent Logic: Custom fallback pattern matching with Python re

Deployment: Hosted on Render (visit demo)

CORS: Enabled for cross-origin frontend-backend communication

Usage
You can interact with the app either by:

Using the UI in the live demo or your local deployment.

Sending chat commands (post requests to /agent) with commands like:

add buy milk

mark task 2 done

delete all done tasks

list tasks

The backend will interpret these commands and perform corresponding task actions.

Installation & Setup (Local)
bash
git clone <your-repo-url>
cd <repo-folder>
python -m venv venv
# Activate venv (Linux/Mac)
source venv/bin/activate
# Activate venv (Windows)
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Visit http://localhost:8000 in your browser to interact with the app.

Project Structure
main.py - FastAPI application including API routes for tasks and AI agent commands.

index.html - Frontend UI served at the root endpoint.

requirements.txt - Python dependencies.

render.yaml - Render deployment configuration (if applicable).
