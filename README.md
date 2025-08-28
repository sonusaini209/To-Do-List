<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List with AI Agent</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #f5f7fa;
            margin: 0;
            padding: 0;
            color: #333;
        }
        header {
            background: #4f46e5;
            color: white;
            padding: 2rem;
            text-align: center;
        }
        header h1 {
            margin: 0;
            font-size: 2.5rem;
        }
        header p {
            font-size: 1.1rem;
            margin-top: 0.5rem;
        }
        .container {
            max-width: 900px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        section {
            background: white;
            border-radius: 12px;
            padding: 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        }
        h2 {
            color: #4f46e5;
            margin-top: 0;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 1rem;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 0.75rem;
            text-align: left;
        }
        th {
            background-color: #4f46e5;
            color: white;
        }
        pre {
            background: #f0f0f0;
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
        }
        a {
            color: #4f46e5;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        .command-section pre {
            background: #e0e7ff;
        }
        footer {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: #666;
        }
    </style>
</head>
<body>
    <header>
        <h1>📝 To-Do List with AI Agent</h1>
        <p>Powerful task management with AI-powered natural language commands. Built for Foyr AI Hackathon 2025.</p>
    </header>

    <div class="container">
        <section>
            <h2>🎯 Project Overview</h2>
            <p>This app lets you manage tasks in two ways:</p>
            <ul>
                <li><strong>Manual Task Control:</strong> Intuitive UI for adding, completing, and deleting tasks.</li>
                <li><strong>AI Control:</strong> Regex-based natural language fallback agent to understand commands.</li>
            </ul>
            <p>All functionalities are accessible in both modes for a seamless experience.</p>
        </section>

        <section>
            <h2>✨ Features</h2>
            <table>
                <tr>
                    <th>Feature</th>
                    <th>Description</th>
                </tr>
                <tr>
                    <td>✅ Task Management</td>
                    <td>Add, complete, delete, and list tasks manually or via AI commands</td>
                </tr>
                <tr>
                    <td>🤖 Simple AI Agent</td>
                    <td>Understands commands via regex-based natural language fallback</td>
                </tr>
                <tr>
                    <td>🔁 Conversation History</td>
                    <td>Tracks the latest 10 user-agent interactions</td>
                </tr>
                <tr>
                    <td>🎨 Dual-Mode Parity</td>
                    <td>Same functionalities accessible via UI or AI chat</td>
                </tr>
                <tr>
                    <td>🚀 Lightweight & Self-Hosted</td>
                    <td>No external AI API; runs fully with minimal dependencies</td>
                </tr>
            </table>
        </section>

        <section>
            <h2>💬 Supported Commands</h2>
            <div class="command-section">
                <h3>Add Task</h3>
                <pre>
add buy groceries
create task read book
                </pre>

                <h3>Complete Task</h3>
                <pre>
mark task 2 done
complete task 1
                </pre>

                <h3>Delete Completed Tasks</h3>
                <pre>
delete all done tasks
                </pre>

                <h3>List Tasks</h3>
                <pre>
list my tasks
show tasks
                </pre>
            </div>
        </section>

        <section>
            <h2>🚀 Setup & Run Locally</h2>
            <pre>
# Clone the repository
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

# Create a virtual environment
python -m venv venv

# Activate the environment
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn main:app --reload
            </pre>
            <p>Open your browser at <a href="http://localhost:8000">http://localhost:8000</a> to start using the app.</p>
        </section>

        <section>
            <h2>🌐 Live Demo</h2>
            <p>Try it live: <a href="#">Click to Open</a></p>
        </section>
    </div>

    <footer>
        &copy; 2025 Foyr AI Hackathon | To-Do List with AI Agent
    </footer>
</body>
</html>
