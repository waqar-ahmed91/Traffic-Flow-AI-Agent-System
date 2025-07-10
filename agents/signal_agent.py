from crewai import Agent
from tools.signal_tools import recommend_signal_timing

class TrafficSignalAgent(Agent):
    def __init__(self, llm):
        super().__init__(
            name="Traffic Signal Optimization Agent",
            role="Signal Timing Recommender",
            goal="Generate optimized traffic signal timings based on congestion severity and disruption events.",
            backstory="An AI traffic engineer using real-time congestion data and simulation modeling to optimize traffic light phases dynamically.",
            llm=llm
        )
