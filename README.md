<h1 align="center">To-Do List with AI Agent — Foyr AI Hackathon 2025</h1>

<p align="center">
  <a href="https://to-do-list-7e75.onrender.com/">
    <img alt="Live Demo" src="https://img.shields.io/badge/Live-Demo-blue" />
  </a>
  &nbsp;
  <a href="https://github.com//sonusaini209/To-Do-List">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/GitHub-Repository-black" />
  </a>
  &nbsp;
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-blue" />
  &nbsp;
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-0.70+-green" />
  &nbsp;
  <img alt="License MIT" src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

---

<p align="center">
  <em>A lightweight to-do list with AI-powered agent interface using fallback pattern matching.<br />
  Dual-mode interaction with full parity: manual UI and natural language commands.</em>
</p>

---

## ✨ Overview

This project was developed for the **Foyr AI Hackathon 2025**, aiming to build **agentic design intelligence** tools that blend a traditional UI with AI agent control.

Users can manage tasks by:

- Manual interaction through a simple UI  
- Natural language commands sent to an AI agent powered by fallback regex matching (no external LLMs required)  
- Viewing conversation history to maintain context

---

## 🛠️ Features

| Feature                 | Description                                              |
|-------------------------|----------------------------------------------------------|
| Task Management         | Add, complete, delete, and list tasks both manually and via AI commands |
| AI Agent Logic          | Lightweight regex-based natural language understanding    |
| Conversation History    | Tracks last 10 user-agent messages for context            |
| Dual Interaction Modes  | Seamless parity between manual UI & AI agent commands     |
| Lightweight Backend     | Python + FastAPI with minimal dependencies                |

---

## 🚀 Usage

### Live Demo

[https://to-do-list-7e75.onrender.com/](https://to-do-list-7e75.onrender.com/)

### Supported Commands Examples

- `add buy groceries`  
- `mark task 1 done`  
- `delete all done tasks`  
- `list tasks`

All commands are also available via manual UI controls.

---

## 💻 Local Setup
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

text

Open [http://localhost:8000](http://localhost:8000) in your browser.



-

## 📄 License

Released under the [MIT License](https://opensource.org/licenses/MIT).

---
