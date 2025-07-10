from crewai.tools import tool

from pydantic import BaseModel
from typing import List, Dict, Any

class CongestionInput(BaseModel):
    sensor_data: List[Dict[str, Any]]

@tool("DetectCongestion")
def detect_congestion(sensor_data: List[Dict[str, Any]]):
    """Analyze traffic sensor data and return congestion status per intersection."""
    result = []
    for entry in sensor_data:
        speed = entry.get("avg_speed_kmh", 0)
        if speed < 20:
            status = "Severe"
        elif speed < 30:
            status = "Moderate"
        else:
            status = "Free Flow"
        result.append({
            "intersection": entry["intersection"],
            "status": status,
            "speed": speed,
            "vehicle_count": entry.get("vehicle_count", 0)
        })
    return result
