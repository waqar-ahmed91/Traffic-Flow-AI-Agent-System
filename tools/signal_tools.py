from crewai.tools import tool

from pydantic import BaseModel
from typing import List, Dict, Any

class SignalInput(BaseModel):
    congestion_data: List[Dict[str, Any]]
    disruptions: List[Dict[str, Any]]

@tool("RecommendSignalTiming")
def recommend_signal_timing(congestion_data: List[Dict[str, Any]], disruptions: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate signal timing recommendations based on congestion and disruptions.
    """
    recommendations = []

    for intersection in congestion_data:
        name = intersection.get("intersection")
        status = intersection.get("status", "Free Flow")

        # Default timings
        green = 30
        red = 30

        # Adjust timings based on congestion
        if status == "Severe":
            green = 50
            red = 20
        elif status == "Moderate":
            green = 40
            red = 30

        # Adjust if disruption is reported at this intersection
        for d in disruptions:
            if d.get("location") == name:
                green = max(green - 5, 15)
                red += 5

        recommendations.append({
            "intersection": name,
            "recommended_green_sec": green,
            "recommended_red_sec": red,
            "status": status
        })

    return {"signal_plan": recommendations}