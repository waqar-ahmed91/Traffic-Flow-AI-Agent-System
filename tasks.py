from crewai import Task

# Import tools
from tools.sensor_tools import get_traffic_sensor_data
from tools.congestion_tools import detect_congestion
from tools.incident_tools import get_disruption_events
from tools.signal_tools import recommend_signal_timing
from tools.transit_tools import check_transit_conflicts
from tools.citizen_tools import process_citizen_reports
from tools.report_tools import generate_traffic_report


def define_traffic_tasks(agents):
    sensor_agent, congestion_agent, incident_agent, signal_agent, public_agent, citizen_agent, report_agent = agents

    task1 = Task(
        description="Collect and normalize traffic sensor data from city intersections including vehicle count, speed, and incident count.",
        agent=sensor_agent,
        tools=[get_traffic_sensor_data],
        expected_output=(
            "Normalized traffic dataset for current time window with fields: "
            "intersection, timestamp, vehicle_count, avg_speed_kmh, incidents."
        )
    )

    task2 = Task(
        description=(
        "Analyze the provided traffic sensor dataset to detect congestion. "
        "You will receive a dictionary with a key 'sensor_data'. "
        "Use the 'DetectCongestion' tool and pass it as: "
        "{ \"sensor_data\": [ ... ] }"
        ),
        agent=congestion_agent,
        tools=[detect_congestion],
        context=[task1],
        expected_output=(
            "List of intersections with congestion scores and status "
            "(e.g., Severe, Moderate, Free Flow)."
        )
    )

    task3 = Task(
        description="Identify current disruptions affecting traffic such as accidents, construction work, or events using mock feeds.",
        agent=incident_agent,
        tools=[get_disruption_events],
        context=[task2],
        expected_output=(
            "Structured list of disruptions with location, type (accident, roadwork, etc.), "
            "start time, and expected duration."
        )
    )

    task4 = Task(
        description="Generate traffic signal timing proposals for congested intersections considering current congestion and disruptions.",
        agent=signal_agent,
        tools=[recommend_signal_timing],
        context=[task2, task3],
        expected_output=(
            "Optimized signal plan per intersection with recommended green and red light durations."
        )
    )

    task5 = Task(
        description="Check public transportation routes for conflicts with congested or disrupted areas and propose mitigation strategies.",
        agent=public_agent,
        tools=[check_transit_conflicts],
        context=[task2, task3],
        expected_output=(
            "List of affected bus/train routes with conflict intersections and suggestions "
            "(e.g., reroute or signal priority)."
        )
    )

    task6 = Task(
        description="Parse citizen reports to extract frequent complaints and correlate them with known congestion or incident areas.",
        agent=citizen_agent,
        tools=[process_citizen_reports],
        context=[task2, task3],
        expected_output=(
            "Ranked list of citizen-reported issues by area, issue type, and severity "
            "with alignment to system data."
        )
    )

    task7 = Task(
        description=(
            "Summarize findings into a markdown traffic report. "
            "You will be given the following structured inputs: "
            "`congestion_data`, `disruptions`, `signal_plans`, `transit_issues`, and `citizen_reports`. "
            "Use the 'GenerateTrafficReport' tool and pass it like:\n"
            "{ \"congestion_data\": [...], \"disruptions\": [...], \"signal_plans\": [...], "
            "\"transit_issues\": [...], \"citizen_reports\": [...] }"
        ),
        agent=report_agent,
        tools=[generate_traffic_report],
        context=[task2, task3, task4, task5, task6],
        expected_output=(
            "A full markdown report summarizing today's traffic conditions, congestion, incidents, "
            "signal plans, transit issues, and citizen complaints for city planners."
        )
    )


    return [task1, task2, task3, task4, task5, task6, task7]
