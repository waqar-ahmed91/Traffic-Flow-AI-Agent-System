from crewai import Agent
from tools.transit_tools import check_transit_conflicts
class PublicTransportAgent(Agent):
    def __init__(self, llm):
        super().__init__(
            name="Public Transport Agent",
            role="Transit Synchronization Analyst",
            goal="Coordinate signal adjustments with public transportation routes to avoid transit delays.",
            backstory="An experienced transit planner focused on aligning bus/train timetables with road signal optimizations for multimodal efficiency.",

            llm=llm
        )