import json
import subprocess
from datetime import datetime

# Path to Suricata alerts
ALERT_FILE = "/var/log/suricata/eve.json"

latest_alert = None

# Read Suricata log
with open(ALERT_FILE, "r") as f:
    lines = f.readlines()

# Find the latest alert
for line in reversed(lines):
    event = json.loads(line)

    if event.get("event_type") == "alert":
        latest_alert = event
        break

# If an alert is found
if latest_alert:

    signature = latest_alert["alert"]["signature"]
    severity = latest_alert["alert"]["severity"]
    src_ip = latest_alert["src_ip"]
    dest_ip = latest_alert["dest_ip"]

    prompt = f"""
You are a professional SOC Analyst.

Analyze the following Suricata alert.

Alert:
{signature}

Source IP:
{src_ip}

Destination IP:
{dest_ip}

Severity:
{severity}

Provide the following:

1. Incident Summary
2. Severity Explanation
3. Investigation Steps
4. Recommended Action
"""

    # Send alert to Ollama
    result = subprocess.run(
        ["ollama", "run", "llama3.2:3b", prompt],
        capture_output=True,
        text=True
    )

    # Display AI response
    print(result.stdout)

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Report filename
    report_file = f"reports/incident_{timestamp}.txt"

    # Save report
    with open(report_file, "w") as report:

        report.write("=" * 60 + "\n")
        report.write("AI SOC INCIDENT REPORT\n")
        report.write("=" * 60 + "\n\n")

        report.write(f"Date: {timestamp}\n\n")
        report.write(f"Alert: {signature}\n")
        report.write(f"Severity: {severity}\n")
        report.write(f"Source IP: {src_ip}\n")
        report.write(f"Destination IP: {dest_ip}\n\n")

        report.write("AI ANALYSIS\n")
        report.write("-" * 60 + "\n")
        report.write(result.stdout)

    print("\n====================================")
    print("Report saved successfully!")
    print(f"Location: {report_file}")
    print("====================================")

else:
    print("No Suricata alerts found.")
