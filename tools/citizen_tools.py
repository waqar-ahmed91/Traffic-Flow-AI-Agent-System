from crewai.tools import tool


@tool("ProcessCitizenReports")
def process_citizen_reports():
    """Analyze citizen-submitted reports and return structured insights."""
    return [
        {"area": "Main St", "issue": "Signal failure", "severity": "High"},
        {"area": "Elm Rd", "issue": "Illegal parking", "severity": "Medium"}
    ]
