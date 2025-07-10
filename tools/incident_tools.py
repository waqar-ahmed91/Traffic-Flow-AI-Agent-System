from crewai.tools import tool


@tool("GetDisruptionEvents")
def get_disruption_events():
    """Simulate traffic disruptions such as accidents, construction, and events."""
    return [
        {"location": "Elm Rd & Oak St", "type": "Accident", "start_time": "08:15", "duration_min": 45},
        {"location": "7th Ave & Pine St", "type": "Roadwork", "start_time": "07:30", "duration_min": 120}
    ]
