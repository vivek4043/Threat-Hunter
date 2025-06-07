# Threat-Hunter

# 🚨 Login-Time Threat Hunter

This project detects suspicious user login activity outside of normal working hours (9am–6pm) for both Linux and Windows systems.

## 📌 Objective
Identify possible insider threats or unauthorized access based on unusual login times.

## 🐧 Linux Usage

### 🔧 Script: `linux/detect_suspicious_logins.py`

- Parses `/var/log/auth.log`
- Finds login activity outside working hours

#### 🛠️ Run
```bash
sudo python3 detect_suspicious_logins.py
```

## 🪟 Windows Usage

### 1️⃣ Export Events

Run this PowerShell script to export login data:
```powershell
.\windows\export_logins.ps1
```

### 2️⃣ Analyze

Run the Python analyzer:
```bash
python windows/analyze_logins.py
```

## ⏰ Configurable

You can modify working hours in the scripts by changing:
```python
WORK_HOURS = (9, 18)
```

## 📦 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```

Only `pandas` is required:
```
pandas
```

## 🧠 Learning Outcome
- Log parsing
- Threat detection logic
- Platform-specific log handling
