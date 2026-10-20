# agent.py
# ADK Web entry point - ADK discovers root_agent from this file

import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Load .env so GOOGLE_API_KEY is available for Gemini
try:
    from dotenv import load_dotenv
    load_dotenv(os.path.join(project_root, ".env"))
except ImportError:
    pass  # python-dotenv not installed — key must be set in environment

from agents.supervisor_agent import supervisor_agent

root_agent = supervisor_agent
