from crewai import Agent
from tools.congestion_tools import detect_congestion

class CongestionDetectionAgent(Agent):
    def __init__(self, llm):
        super().__init__(
            name="Congestion Detection Agent",
            role="Traffic Flow Analyzer",
            goal="Analyze traffic sensor patterns to identify current and emerging congestion hotspots.",
            backstory="A transportation analyst trained in traffic modeling, anomaly detection, and congestion trend forecasting using real-time sensor data.",
            llm=llm
        )