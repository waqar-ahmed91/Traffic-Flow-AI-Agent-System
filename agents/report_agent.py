from crewai import Agent
from tools.report_tools import generate_traffic_report

class TrafficReportAgent(Agent):
    def __init__(self, llm):
        super().__init__(
            role="Urban Traffic Report Compiler",
            goal="Generate markdown reports summarizing traffic, congestion, and optimization strategies.",
            backstory="A veteran urban planner with experience in interpreting complex traffic data.",
            llm=llm,
            verbose=True,
            enforce_format=True  # ✅ Force use of correct tool syntax
        )
