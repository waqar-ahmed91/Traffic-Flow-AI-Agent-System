import json
from pathlib import Path
from datetime import datetime, timedelta

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

now = datetime.now()

def write_json(filename, content):
    with open(DATA_DIR / filename, "w") as f:
        json.dump(content, f, indent=2)

def write_md(filename, content):
    with open(DATA_DIR / filename, "w") as f:
        f.write(content)

# 1. Sensor Data
sensor_data = [
    {
        "intersection": "5th Ave & Main St",
        "timestamp": (now - timedelta(minutes=10)).isoformat(timespec="minutes"),
        "vehicle_count": 160,
        "avg_speed_kmh": 22.5,
        "incidents": 0
    },
    {
        "intersection": "Elm Rd & Oak St",
        "timestamp": (now - timedelta(minutes=5)).isoformat(timespec="minutes"),
        "vehicle_count": 190,
        "avg_speed_kmh": 17.8,
        "incidents": 1
    },
    {
        "intersection": "7th Ave & Pine St",
        "timestamp": now.isoformat(timespec="minutes"),
        "vehicle_count": 130,
        "avg_speed_kmh": 25.1,
        "incidents": 0
    }
]
write_json("mock_sensor_data.json", sensor_data)

# 2. Congestion Output
congestion_output = [
    {
        "intersection": "Elm Rd & Oak St",
        "congestion_score": 0.58,
        "status": "Severe"
    },
    {
        "intersection": "5th Ave & Main St",
        "congestion_score": 0.33,
        "status": "Moderate"
    }
]
write_json("mock_congestion_output.json", congestion_output)

# 3. Incident Events
incidents = [
    {
        "event_type": "Accident",
        "location": "Elm Rd & Oak St",
        "start_time": (now - timedelta(minutes=5)).isoformat(timespec="minutes"),
        "expected_duration_min": 60
    },
    {
        "event_type": "Roadwork",
        "location": "7th Ave & Pine St",
        "start_time": (now - timedelta(hours=1)).isoformat(timespec="minutes"),
        "expected_duration_min": 180
    }
]
write_json("mock_incidents.json", incidents)

# 4. Signal Plan
signal_plan = [
    {"intersection": "Elm Rd & Oak St", "green_sec": 80, "red_sec": 40},
    {"intersection": "5th Ave & Main St", "green_sec": 60, "red_sec": 60}
]
write_json("mock_signal_plan.json", signal_plan)

# 5. Transit Routes & Conflicts
routes = {
    "Bus 17": ["Elm Rd & Oak St", "7th Ave & Pine St"],
    "Bus 42": ["5th Ave & Main St"]
}
write_json("mock_transit_routes.json", routes)

conflicts = [
    {
        "route_id": "Bus 17",
        "conflict_intersections": ["Elm Rd & Oak St"],
        "suggested_adjustments": "Increase green time or create transit priority lane"
    }
]
write_json("mock_transit_conflicts.json", conflicts)

# 6. Citizen Reports
citizen_reports = [
    {
        "area": "Downtown",
        "common_issues": ["Blocked signal", "Heavy traffic"],
        "severity_level": "High"
    },
    {
        "area": "Midtown",
        "common_issues": ["Malfunctioning light"],
        "severity_level": "Medium"
    }
]
write_json("mock_citizen_reports.json", citizen_reports)

# 7. Final Report (Markdown)
final_report_md = f"""# Daily Traffic Flow Optimization Report

## Summary
- 3 sensor points processed
- 2 congestion hotspots
- 2 incident reports

## Congestion Overview
- Elm Rd & Oak St: Severe (0.58)
- 5th Ave & Main St: Moderate (0.33)

## Incidents
- Accident at Elm Rd & Oak St for 60 mins
- Roadwork at 7th Ave & Pine St for 180 mins

## Signal Proposals
- Elm Rd & Oak St: Green 80s, Red 40s
- 5th Ave & Main St: Green 60s, Red 60s

## Transit Conflicts
- Route Bus 17 conflicts at Elm Rd & Oak St

## Citizen Feedback
- Downtown: Blocked signal, Heavy traffic (Severity: High)
- Midtown: Malfunctioning light (Severity: Medium)

## Final Recommendations
- Deploy optimized signal timings.
- Notify public transit operators.
- Resolve critical citizen complaints.
"""
write_md("mock_final_report.md", final_report_md)

print("Mock data files generated in /data")
