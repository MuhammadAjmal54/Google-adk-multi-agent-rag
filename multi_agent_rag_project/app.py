# app.py
# Main entry point for Google ADK Multi-Agent Application

import sys
import os

# Project root directory ko path mein add karo
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from agents.supervisor_agent import supervisor_agent

# ✅ ADK ko 'app' variable chahiye jo root agent ho
app = supervisor_agent

if __name__ == "__main__":
    print(" Multi-Agent RAG Application")
    print("=" * 50)
    print(f"Root Agent: {app.name}")
    print(f"Model: {app.model}")
    print(f"Sub-agents: {[a.name for a in app.sub_agents]}")
    print("=" * 50)
    print("\n[TIP] Run with: adk web")