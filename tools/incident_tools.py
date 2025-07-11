from crewai.tools import tool
from typing import List, Dict, Any
from pydantic import BaseModel

class DisruptionEvent(BaseModel):
    location: str
    type: str  # e.g., Accident, Roadwork
    start_time: str  # Ideally in "HH:MM" format
    duration_min: int  # Duration in minutes


@tool("GetDisruptionEvents")
def get_disruption_events() -> List[Dict[str, Any]]:
    """
    Simulate traffic disruptions such as accidents, roadworks, and events.
    Returns a list of disruption dictionaries including location, type, start time, and duration.
    """
    return [
        {
            "location": "Elm Rd & Oak St",
            "type": "Accident",
            "start_time": "08:15",
            "duration_min": 45
        },
        {
            "location": "7th Ave & Pine St",
            "type": "Roadwork",
            "start_time": "07:30",
            "duration_min": 120
        }
    ]
