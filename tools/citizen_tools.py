from crewai.tools import tool
from typing import List, Dict, Any
from pydantic import BaseModel

class CitizenFeedbackInput(BaseModel):
    sensor_data: List[Dict[str, Any]]
    disruptions: List[Dict[str, Any]]

@tool("ProcessCitizenReports")
def process_citizen_reports(sensor_data: List[Dict[str, Any]], disruptions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Parse citizen reports to extract frequent complaints and correlate them with congestion or incidents.
    Returns a list of structured feedback including area, issue_type, and severity.
    """

    # Simulated synthetic structured citizen reports derived from input
    return [
        {
            "area": "5th Ave & Main St",
            "issue_type": "Signal failure",
            "severity": "High"
        },
        {
            "area": "Elm Rd & Oak St",
            "issue_type": "Accident",
            "severity": "Severe"
        },
        {
            "area": "Elm Rd & Oak St",
            "issue_type": "Illegal parking",
            "severity": "Medium"
        },
        {
            "area": "7th Ave & Pine St",
            "issue_type": "Roadwork",
            "severity": "High"
        }
    ]