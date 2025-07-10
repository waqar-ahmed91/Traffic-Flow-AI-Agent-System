from crewai.tools import tool
from pydantic import BaseModel
from typing import List, Dict, Any

class ReportInput(BaseModel):
    congestion_data: List[Dict[str, Any]]
    disruptions: List[Dict[str, Any]]
    signal_plan: List[Dict[str, Any]]
    transit_issues: List[Dict[str, Any]]
    citizen_feedback: List[Dict[str, Any]]

@tool("GenerateTrafficReport")
def generate_traffic_report(
    congestion_data: List[Dict[str, Any]],
    disruptions: List[Dict[str, Any]],
    signal_plan: List[Dict[str, Any]],
    transit_issues: List[Dict[str, Any]],
    citizen_feedback: List[Dict[str, Any]],
) -> str:
    """
    Generate a markdown report based on congestion, disruptions, signal plans, transit issues, and citizen feedback.
    """

    report = "# 🚦 Urban Traffic Optimization Report\n\n"

    report += "## 🔴 Congestion Summary\n"
    for item in congestion_data:
        report += f"- **{item.get('intersection')}**: {item.get('status')}\n"

    report += "\n## 🚧 Disruption Events\n"
    for d in disruptions:
        report += f"- **{d.get('location')}** ({d.get('type')}): Duration {d.get('duration')}\n"

    report += "\n## 🟢 Signal Timing Recommendations\n"
    for s in signal_plan:
        report += f"- **{s.get('intersection')}**: Green={s.get('recommended_green_sec')}s, Red={s.get('recommended_red_sec')}s\n"

    report += "\n## 🚍 Transit Impact\n"
    for t in transit_issues:
        report += f"- **{t.get('route')}** conflict at {t.get('conflict')} — Suggestion: {t.get('suggestion')}\n"

    report += "\n## 📣 Citizen Feedback Highlights\n"
    for c in citizen_feedback:
        report += f"- **{c.get('area')}**: {c.get('issue_type')} (Severity: {c.get('severity')})\n"

    report += "\n---\n_Report generated automatically by the AI Traffic Monitoring System._"

    return report

