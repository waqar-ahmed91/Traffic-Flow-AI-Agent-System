from markdown import markdown
from weasyprint import HTML

css = """
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
"""
md_text = """
# Urban Traffic Report Summary

## Congestion Summary
- **5th Ave & Main St**: Moderate, Speed 22.5 km/h, Vehicle Count 160
- **Elm Rd & Oak St**: Severe, Speed 17.8 km/h, Vehicle Count 190
- **7th Ave & Pine St**: Moderate, Speed 25.1 km/h, Vehicle Count 130

## Disruption Events
- **Elm Rd & Oak St** (Accident): Started at 08:15, Expected Duration 45 minutes
- **7th Ave & Pine St** (Roadwork): Started at 07:30, Expected Duration 120 minutes

## Signal Timing Recommendations
- **5th Ave & Main St**: Green Light Duration: 40 seconds, Red Light Duration: 30 seconds
- **Elm Rd & Oak St**: Green Light Duration: 45 seconds, Red Light Duration: 25 seconds (due to accident from 08:15 - 09:00)
- **7th Ave & Pine St**: Green Light Duration: 35 seconds, Red Light Duration: 35 seconds (due to roadwork from 07:30 - 10:30)

## Transit Impact
- **Bus 42**: Conflict at Elm Rd & Oak St — Suggestion: Reroute via Maple Ave
- **Tram A**: Conflict at 7th Ave & Pine St — Suggestion: Schedule a delay of 10 minutes

## Citizen Feedback Highlights
| Area                  | Issue Type    | Severity |
|-----------------------|---------------|----------|
| 5th Ave & Main St     | Signal failure| High     |
| Elm Rd & Oak St       | Accident      | Severe   |
| Elm Rd & Oak St       | Illegal parking| Medium  |
| 7th Ave & Pine St     | Roadwork      | High     |
"""
md_path = "output/traffic_report_2025-07-11_22-24.md"
# Step 1: Read markdown from file
with open(md_path, "r", encoding="utf-8") as f:
    md_content = f.read()

# Step 2: Convert markdown to HTML
html_body = markdown(md_content, extensions=["tables", "extra", "sane_lists"])
# html_body = markdown(md_text, extensions=['tables', 'extra'])
html_template = f"<!DOCTYPE html><html><head>{css}</head><body>{html_body}</body></html>"
HTML(string=html_template).write_pdf("report.pdf")

