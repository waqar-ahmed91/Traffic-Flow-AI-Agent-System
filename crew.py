import argparse
from crewai import Crew
from langchain_community.chat_models import ChatOpenAI
from langchain_ollama import OllamaLLM
from agents.sensor_agent import SensorDataAgent
from agents.congestion_agent import CongestionDetectionAgent
from agents.incident_agent import IncidentEventAgent
from agents.signal_agent import TrafficSignalAgent
from agents.public_transport_agent import PublicTransportAgent
from agents.citizen_agent import CitizenReportAgent
from agents.report_agent import TrafficReportAgent

# Task logic
from tasks import define_traffic_tasks

def get_llm(mock=False):
    if mock:
        return OllamaLLM(model="ollama/granite3-dense:2b", base_url="http://localhost:11434", temperature=0.1)
    else:
        return ChatOpenAI(model_name="gpt-4", temperature=0.1)


class TrafficFlowCrew:
    def __init__(self, use_mock=False):
        self.use_mock = use_mock
        self.llm = get_llm(mock=self.use_mock)

        # Initialize agents with LLM + mock switch
        self.sensor_agent = SensorDataAgent(llm=self.llm)
        self.congestion_agent = CongestionDetectionAgent(llm=self.llm)
        self.incident_agent = IncidentEventAgent(llm=self.llm)
        self.signal_agent = TrafficSignalAgent(llm=self.llm)
        self.public_transport_agent = PublicTransportAgent(llm=self.llm)
        self.citizen_agent = CitizenReportAgent(llm=self.llm)
        self.report_agent = TrafficReportAgent(llm=self.llm)

    def run(self):
        agents = [
            self.sensor_agent,
            self.congestion_agent,
            self.incident_agent,
            self.signal_agent,
            self.public_transport_agent,
            self.citizen_agent,
            self.report_agent
        ]

        print(f"[INFO] Initializing {'🧪 MOCK' if self.use_mock else '🔌 LIVE'} Crew run with {len(agents)} agents...")

        # Define tasks for Crew
        tasks = define_traffic_tasks(agents)

        # Assemble and execute crew
        crew = Crew(
            agents=agents,
            tasks=tasks,
            verbose=True
        )
        crew.kickoff()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Traffic Flow Agent System")
    parser.add_argument('--mock', action='store_true', help='Use mock data and offline logic')
    args = parser.parse_args()

    TrafficFlowCrew(use_mock=args.mock).run()
