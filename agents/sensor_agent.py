from crewai import Agent
from tools.sensor_tools import get_traffic_sensor_data
class SensorDataAgent(Agent):
    def __init__(self, llm):
        super().__init__(
            name="Sensor Data Agent",
            role="Traffic Sensor Reader",
            goal="Parse and normalize traffic sensor data including speed, vehicle counts, and incidents from multiple intersections.",
            backstory="An expert in urban mobility systems, specialized in collecting and normalizing IoT sensor data for traffic control infrastructure.",
            llm=llm
        )

