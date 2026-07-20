# 🛡️ AI-Powered SOC Analyst Assistant

An AI-powered Security Operations Center (SOC) assistant that automates the analysis of Suricata IDS alerts using a locally hosted Large Language Model (Llama 3 via Ollama). The project helps security analysts quickly understand alerts by generating incident summaries, severity assessments, investigation steps, and recommended actions.

---

## 📌 Features

- Detects network attacks using Suricata IDS
- Reads alerts from Suricata's `eve.json`
- Uses Llama 3 (Ollama) for AI-based alert analysis
- Generates incident reports automatically
- Simulates attacks using Kali Linux (Nmap, ICMP)
- Works completely offline with a local AI model

---

## 🏗️ Project Architecture

```
Kali Linux
     │
     ▼
Network Traffic
     │
     ▼
Suricata IDS
     │
     ▼
eve.json
     │
     ▼
Python Script
     │
     ▼
Ollama + Llama 3
     │
     ▼
AI Incident Report
```

---

## 🛠️ Technologies Used

- Python
- Suricata IDS
- Ollama
- Llama 3
- Ubuntu Linux
- Kali Linux
- VMware

---

## 📂 Project Structure

```
AI-Powered-SOC-Analyst-Assistant/
│
├── ai_soc_assistant.py
├── read_alert.py
├── README.md
├── .gitignore
└── reports/
```

---

## 🚀 Workflow

1. Generate network traffic from Kali Linux.
2. Suricata detects suspicious activity.
3. Alerts are stored in `eve.json`.
4. Python extracts the latest alert.
5. Llama 3 analyzes the alert.
6. An incident report is generated automatically.

---

## 📋 Sample AI Output

- Incident Summary
- Severity Assessment
- Investigation Steps
- Recommended Actions

---

## 🎯 Skills Demonstrated

- Security Operations Center (SOC)
- Network Security Monitoring
- Intrusion Detection
- Incident Analysis
- AI in Cybersecurity
- Python Automation
- Linux Administration

---

## 🔮 Future Improvements

- MITRE ATT&CK Mapping
- Risk Score Calculation
- PDF Report Generation
- Streamlit Dashboard
- Database Storage (SQLite)
- Email Notifications

---

## 👨‍💻 Author

**Abinaya S**

Cyber Security Student | SOC Analyst Enthusiast

GitHub: https://github.com/abinaya-63
