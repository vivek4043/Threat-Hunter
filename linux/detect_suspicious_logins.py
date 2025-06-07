import re
from datetime import datetime
from alert_email import send_alert

log_path = "/var/log/auth.log"
WORK_HOURS = (9, 18)
login_pattern = re.compile(r'^(\w+\s+\d+\s+\d+:\d+:\d+).*session opened for user (\w+)')
suspicious_logins = []

with open(log_path, "r") as file:
    for line in file:
        match = login_pattern.search(line)
        if match:
            time_str, user = match.groups()
            log_time = datetime.strptime(time_str, "%b %d %H:%M:%S").replace(year=datetime.now().year)
            if log_time.hour < WORK_HOURS[0] or log_time.hour > WORK_HOURS[1]:
                formatted_time = log_time.strftime("%Y-%m-%d %H:%M:%S")
                suspicious_logins.append((formatted_time, user))
                send_alert(
                    subject="⚠️ Suspicious Login Detected",
                    body=f"User '{user}' logged in at {formatted_time} (outside working hours)."
                )

print("⚠️ Suspicious Logins (Linux):\n")
for time, user in suspicious_logins:
    print(f"{time} - {user}")
