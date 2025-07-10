import json
import os
from crewai.tools import tool


@tool("GetTrafficSensorData")
def get_traffic_sensor_data(mock: bool = False):
    """Load or fetch current traffic sensor data from intersections."""
    if mock:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(base_dir, 'data', 'mock_sensor_data.json')
        if os.path.exists(data_path):
            with open(data_path, 'r') as f:
                data = json.load(f)
                return {"sensor_data": data}
        else:
            return {"error": f"Mock file not found at {data_path}"}
    return {"sensor_data": [{"intersection": "Mocked from live API", "vehicle_count": 100, "avg_speed_kmh": 25.0, "incidents": 0}]}
