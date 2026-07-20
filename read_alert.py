import json

alert_file = "/var/ossec/logs/alerts/alerts.json"

with open(alert_file, "r") as f:
    lines = f.readlines()

last_alert = json.loads(lines[-1])

print("Rule Description:")
print(last_alert["rule"]["description"])

print("\nRule Level:")
print(last_alert["rule"]["level"])

print("\nAgent Name:")
print(last_alert["agent"]["name"])
