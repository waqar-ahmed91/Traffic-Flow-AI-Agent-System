from crewai.tools import tool
from pydantic import BaseModel
from typing import List, Dict, Any

class ReportInput(BaseModel):
    congestion_data: List[Dict[str, Any]]
    disruptions: List[Dict[str, Any]]
    signal_plan: List[Dict[str, Any]]
    transit_issues: List[Dict[str, Any]]
    citizen_feedback: List[Dict[str, Any]]

# @tool("GenerateTrafficReport")
# def generate_traffic_report(
#     congestion_data: List[Dict[str, Any]],
#     disruptions: List[Dict[str, Any]],
#     signal_plan: List[Dict[str, Any]],
#     transit_issues: List[Dict[str, Any]],
#     citizen_feedback: List[Dict[str, Any]],
# ) -> str:
#     """
#     Generate a markdown report based on congestion, disruptions, signal plans, transit issues, and citizen feedback.
#     """

#     report = "# 🚦 Urban Traffic Optimization Report\n\n"

#     report += "## 🔴 Congestion Summary\n"
#     for item in congestion_data:
#         report += f"- **{item.get('intersection')}**: {item.get('status')}\n"

#     report += "\n## 🚧 Disruption Events\n"
#     for d in disruptions:
#         report += f"- **{d.get('location')}** ({d.get('type')}): Duration {d.get('duration')}\n"

#     report += "\n## 🟢 Signal Timing Recommendations\n"
#     for s in signal_plan:
#         report += f"- **{s.get('intersection')}**: Green={s.get('recommended_green_sec')}s, Red={s.get('recommended_red_sec')}s\n"

#     report += "\n## 🚍 Transit Impact\n"
#     for t in transit_issues:
#         report += f"- **{t.get('route')}** conflict at {t.get('conflict')} — Suggestion: {t.get('suggestion')}\n"

#     report += "\n## 📣 Citizen Feedback Highlights\n"
#     for c in citizen_feedback:
#         report += f"- **{c.get('area')}**: {c.get('issue_type')} (Severity: {c.get('severity')})\n"

#     report += "\n---\n_Report generated automatically by the AI Traffic Monitoring System._"

#     return report


@tool("GenerateTrafficReport")
def generate_traffic_report(
    congestion_data: List[Dict[str, Any]],
    disruptions: List[Dict[str, Any]],
    signal_plan: List[Dict[str, Any]],
    transit_issues: List[Dict[str, Any]],
    citizen_feedback: List[Dict[str, Any]],
) -> str:
    """Generate a clean HTML report for traffic summary."""

    html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Urban Traffic Report</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        font-size: 14px;
                        padding: 20px;
                        color: #333;
                    }
                    h1, h2 {
                        color: #2c3e50;
                        margin-top: 30px;
                    }
                    ul {
                        padding-left: 20px;
                    }
                    li {
                        margin-bottom: 6px;
                    }
                    table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 15px;
                    }
                    th, td {
                        border: 1px solid #ccc;
                        padding: 8px;
                        text-align: left;
                    }
                    th {
                        background-color: #f4f4f4;
                    }
                    em {
                        font-size: 12px;
                        color: #888;
                    }
                </style>
            </head>
            <body>
                <h1>🚦 Urban Traffic Optimization Report</h1>

                <h2>🔴 Congestion Summary</h2>
                <ul>
            """
    for item in congestion_data:
        html += (
            f"<li><strong>{item.get('intersection')}</strong>: "
            f"{item.get('status')}, Speed {item.get('speed')} km/h, "
            f"Vehicle Count {item.get('vehicle_count')}</li>\n"
        )

    html += "</ul>\n<h2>🚧 Disruption Events</h2>\n<ul>"

    for d in disruptions:
        html += (
            f"<li><strong>{d.get('location')}</strong> ({d.get('type')}): "
            f"Started at {d.get('start_time')}, Expected Duration {d.get('duration_min')} minutes</li>\n"
        )

    html += "</ul>\n<h2>🟢 Signal Timing Recommendations</h2>\n<ul>"

    for s in signal_plan:
        html += (
            f"<li><strong>{s.get('intersection')}</strong>:<br>"
            f"&nbsp;&nbsp;Green: {s.get('recommended_green_sec')}s<br>"
            f"&nbsp;&nbsp;Red: {s.get('recommended_red_sec')}s<br>"
            f"&nbsp;&nbsp;Status: {s.get('status', 'N/A')}</li>\n"
        )

    html += "</ul>\n<h2>🚍 Transit Impact</h2>\n<ul>"

    for t in transit_issues:
        html += (
            f"<li><strong>{t.get('route')}</strong>: Conflict at {t.get('conflict')} — "
            f"Suggestion: {t.get('suggestion')}</li>\n"
        )

    html += "</ul>\n<h2>📣 Citizen Feedback Highlights</h2>\n"

    if citizen_feedback:
        html += """
        <table>
            <thead>
                <tr>
                    <th>Area</th>
                    <th>Issue Type</th>
                    <th>Severity</th>
                    <th>Speed (km/h)</th>
                    <th>Vehicle Count</th>
                </tr>
            </thead>
            <tbody>
        """
        for fb in citizen_feedback:
            html += f"""
                <tr>
                    <td>{fb.get("area")}</td>
                    <td>{fb.get("issue_type")}</td>
                    <td>{fb.get("severity")}</td>
                    <td>{fb.get("speed_kmh", "N/A")}</td>
                    <td>{fb.get("vehicle_count", "N/A")}</td>
                </tr>
            """
        html += "</tbody></table>\n"
    else:
        html += "<p>No citizen feedback available.</p>\n"

    html += "<hr><p><em>Report generated automatically by the AI Traffic Monitoring System.</em></p>\n"
    html += "</body></html>"

    return html