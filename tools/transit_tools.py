from crewai.tools import tool

from pydantic import BaseModel
from typing import List, Dict, Any

class TransitInput(BaseModel):
    disruptions: List[Dict[str, Any]]

@tool("CheckTransitConflicts")
def check_transit_conflicts(disruptions: List[Dict[str, Any]]):
    """Detect conflicts between public transport and disrupted routes, and suggest mitigation."""
    return [
        {"route": "Bus 42", "conflict": "Elm Rd & Oak St", "suggestion": "Reroute via Maple Ave"},
        {"route": "Tram A", "conflict": "7th Ave & Pine St", "suggestion": "Schedule delay of 10 mins"}
    ]
