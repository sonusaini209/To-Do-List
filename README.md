<h1 align="center">To-Do List with AI Agent — Foyr AI Hackathon 2025</h1>

<p align="center">
  <a href="https://to-do-list-7e75.onrender.com/">
    <img alt="Live Demo" src="https://img.shields.io/badge/Live-Demo-blue" />
  </a>
  &nbsp;
  <a href="https://github.com/yourusername/yourrepo">
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

git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

text

Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 📂 Project Structure

yourrepo/
├── main.py # Backend API & AI agent logic
├── index.html # Frontend UI served at '/'
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment config (optional)
└── README.md # This file

text

---

## 🔮 Future Improvements

- Integrate full LLM support (OpenAI, Hugging Face, LangChain) for advanced conversational AI  
- Add voice input/output with Whisper, Web Speech API, or Azure Speech Services  
- Persist tasks and chat history with MongoDB or vector databases (Weaviate, Pinecone)  
- Enhance UI using React, Vue, or similar frameworks  
- Develop clean prompt chains with contextual memory for better user experience

---

## 🙌 Acknowledgments

Special thanks to the **Foyr AI** team for the inspiring hackathon opportunity to explore agentic interfaces and AI-native software design.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check [issues page](https://github.com/yourusername/yourrepo/issues) to contribute.

---

## 📄 License

Released under the [MIT License](https://opensource.org/licenses/MIT).

---

*This README was crafted with 💙 for the Foyr AI Hackathon 2025.*

---

<p align="center">
  <a href="https://twitter.com/yourTwitterHandle">Follow me on Twitter</a> &nbsp;|&nbsp;
  <a href="https://github.com/yourusername">GitHub Profile</a>
</p>
