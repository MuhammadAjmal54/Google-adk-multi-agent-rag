# 🤖 Google ADK Multi-Agent RAG System

A multi-agent RAG (Retrieval-Augmented Generation) application built with **Google Agent Development Kit (ADK)** and **Gemini AI**. The system uses a supervisor agent to intelligently route user queries to specialized sub-agents.

## 🏗️ Architecture

```
supervisor_agent  (routes queries)
├── hr_agent         → employee info, salaries, departments
├── knowledge_agent  → company policies, FAQs, working hours
├── finance_agent    → salary increments, bonus calculations, math
└── general_agent    → current date, time, day information
```

## ✨ Features

- **Multi-Agent Routing** — Supervisor automatically routes each query to the right specialist agent
- **HR Queries** — Search employees by name, department, salary range
- **Knowledge Base** — Company policies and FAQs with keyword-based search
- **Finance Calculations** — Salary increments, performance bonuses, math expressions
- **Date & Time** — Real-time date and day information
- **Tool-Enabled Agents** — Each sub-agent has a dedicated tool for data retrieval
- **Gemini Powered** — Uses Google Gemini via the ADK framework

## 🗂️ Project Structure

```
multi_agent_rag_project/
├── agents/
│   ├── supervisor_agent.py   # Routes queries to sub-agents
│   ├── hr_agent.py           # Employee database queries
│   ├── knowledge_agent.py    # Policy & FAQ search
│   ├── finance_agent.py      # Financial calculations
│   └── general_agent.py      # Date & time info
├── tools/
│   ├── hr_tools.py           # query_employee_database()
│   ├── knowledge_tools.py    # search_knowledge()
│   ├── finance_tools.py      # calculate_finance()
│   └── general_tools.py      # get_datetime_info()
├── data/
│   ├── employees.db          # SQLite employee database
│   ├── company_policies.txt  # Company policy documents
│   └── company_faqs.txt      # Company FAQ documents
├── agent.py                  # ADK entry point (root_agent)
├── rag_setup.py              # Optional ChromaDB vector DB setup
├── requirements.txt          # Python dependencies
└── .env                      # API key (not committed)
```

## 🚀 Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/MuhammadAjmal54/Google-adk-multi-agent-rag.git
cd Google-adk-multi-agent-rag/multi_agent_rag_project
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key
Create a `.env` file in the project folder:
```
GOOGLE_API_KEY=your_gemini_api_key_here
```
Get your key from: https://aistudio.google.com/app/apikey

### 5. Run the ADK Web UI
```bash
adk web
```
Open http://127.0.0.1:8000 in your browser.

## 💬 Example Queries

| Query | Routed To |
|---|---|
| "Tell me about Ahmed Khan" | `hr_agent` |
| "What is the leave policy?" | `knowledge_agent` |
| "Calculate 10% increment on 85000" | `finance_agent` |
| "What day is today?" | `general_agent` |
| "How many employees are in Engineering?" | `hr_agent` |
| "What are the working hours?" | `knowledge_agent` |
| "Bonus for salary 90000 with Good rating" | `finance_agent` |

## 🛠️ Tech Stack

- [Google ADK](https://google.github.io/adk-docs/) — Agent Development Kit
- [Gemini AI](https://ai.google.dev/) — LLM backbone
- SQLite — Employee database
- Python 3.12

## 📄 License

MIT License
