from crewai import Agent
from tools.incident_tools import get_disruption_events
class IncidentEventAgent(Agent):
    def __init__(self, llm):
        super().__init__(
            name="Incident and Event Agent",
            role="Disruption Tracker",
            goal="Track and classify road incidents, construction alerts, and public events that affect traffic flow.",
            backstory="Specializes in mining structured and unstructured feeds from news APIs, weather alerts, and municipal calendars to assess disruptions.",
            llm=llm
        )
