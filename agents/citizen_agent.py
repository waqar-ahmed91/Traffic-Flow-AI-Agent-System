from crewai import Agent
from tools.citizen_tools import process_citizen_reports

class CitizenReportAgent(Agent):
    def __init__(self, llm):
        super().__init__(
            name="Citizen Report Agent",
            role="Crowd-Sourced Traffic Issue Analyzer",
            goal="Extract and categorize road issues from citizen complaints like signal outages, potholes, and blockages.",
            backstory="An NLP specialist trained to analyze user-submitted reports, cluster local issues, and identify recurring hotspots from feedback platforms.",
            llm=llm
        )

