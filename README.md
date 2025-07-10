# 🚦 Traffic Flow AI Agent System

A multi-agent AI system built using [CrewAI](https://github.com/joaomdmoura/crewai) that simulates intelligent urban traffic monitoring and optimization. It leverages synthetic or real-time traffic data to detect congestion, analyze incidents, optimize signal timings, assess public transit impact, and generate reports for city planners.

---

## 🧠 Project Overview

This project demonstrates a fully autonomous agentic workflow that:

- Collects and normalizes traffic sensor data
- Detects congestion hotspots across city intersections
- Identifies disruptions (accidents, roadwork, etc.)
- Recommends dynamic signal timing adjustments
- Assesses conflicts with public transportation routes
- Processes citizen complaints for actionable feedback
- Generates a comprehensive markdown traffic report

Each step is executed by a specialized agent with access to relevant tools and context-aware reasoning.

---

## 📂 Directory Structure

traffic_flow_agent/
├── agents/ # All agent definitions
├── tools/ # Modular tools used by agents
├── data/ # Mock or real-time traffic data
│ └── mock_sensor_data.json
├── tasks.py # Task definitions and dependencies
├── crew.py # Crew assembly and execution logic
├── generate_mock_sensor_data.py # Script to generate synthetic sensor data
├── requirements.txt # Dependencies
└── README.md

---

## 🛠 Features

- ✅ Modular agents with isolated responsibilities
- ✅ Real or mock traffic sensor data ingestion
- ✅ Configurable with `--mock` switch for development
- ✅ Tool-based design
- ✅ Fully observable CrewAI execution logs
- ✅ Final report in clean Markdown format

---

## 🚀 Getting Started

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

```bash
python crew.py --mock
```

Use the --mock flag to run in offline mode with mock sensor and disruption data.

## 📡 Agent Overview

| Agent Name                    | Role                                       |
| ----------------------------- | ------------------------------------------ |
| Traffic Sensor Reader         | Loads and normalizes sensor data           |
| Traffic Flow Analyzer         | Detects congestion levels at intersections |
| Incident Event Monitor        | Identifies traffic disruptions from feeds  |
| Traffic Signal Planner        | Recommends optimized signal timings        |
| Transit Conflict Resolver     | Detects public transport route conflicts   |
| Citizen Complaint Analyst     | Parses user reports for recurring issues   |
| Urban Traffic Report Compiler | Generates a final markdown report          |

## 📊 Sample Output

The final output includes sections such as:

🚧 Congestion Hotspots

⚠️ Disruption Timeline

🚦 Signal Timing Proposals

🚌 Public Transport Route Conflicts

📢 Citizen Complaint Insights

All presented in a well-structured Markdown report.

## 📌 Future Extensions

Integration with live traffic APIs

Visualization dashboard using Streamlit or Dash

Real-time notification system for planners

## 🧑‍💻 Author

Developed by Waqar Ahmed
For inquiries or collaboration: [LinkedIn](https://www.linkedin.com/in/waqarnu/)
