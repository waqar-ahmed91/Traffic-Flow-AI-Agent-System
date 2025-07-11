import argparse
import os
import re
from markdown import markdown
from weasyprint import HTML
from datetime import datetime
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
from tasks import define_traffic_tasks

def get_llm(mock=False):
    if mock:
        return OllamaLLM(model="ollama/qwen2.5:7b", base_url="http://localhost:11434", temperature=0.6)
    else:
        return ChatOpenAI(model_name="gpt-4o-mini", temperature=0.6)


class TrafficFlowCrew:
    def __init__(self, use_mock=False):
        self.use_mock = use_mock
        self.llm = get_llm(mock=self.use_mock)

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

        tasks = define_traffic_tasks(agents)

        crew = Crew(
            agents=agents,
            tasks=tasks,
            verbose=True
        )

        final_output = crew.kickoff()
        final_report = final_output.final_output if hasattr(final_output, "final_output") else str(final_output)

        clean_report = final_report.strip()
        if clean_report.startswith("```markdown") or clean_report.startswith("```"):
            clean_report = re.sub(r"^```markdown\s*", "", clean_report)
            clean_report = re.sub(r"\s*```$", "", clean_report)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
        os.makedirs("output", exist_ok=True)
        md_path = f"output/traffic_report_{timestamp}.md"
        pdf_path = f"output/traffic_report_{timestamp}.pdf"

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(clean_report)
        print(f"[INFO] ✅ Markdown saved: {md_path}")
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

        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        html_body = markdown(md_content, extensions=["tables", "extra", "sane_lists"])
        html_template = f"<!DOCTYPE html><html><head>{css}</head><body>{html_body}</body></html>"
        HTML(string=html_template).write_pdf(pdf_path)
        print(f"[INFO] 📄 PDF saved: {pdf_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Traffic Flow Agent System")
    parser.add_argument('--mock', action='store_true', help='Use mock data and offline logic')
    args = parser.parse_args()

    TrafficFlowCrew(use_mock=args.mock).run()
