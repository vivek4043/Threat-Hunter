import pandas as pd
from popup_alert import popup_alert

df = pd.read_csv("logins.csv")
df['TimeCreated'] = pd.to_datetime(df['TimeCreated'])

def is_suspicious(time):
    return time.hour < 9 or time.hour > 18

df['is_suspicious'] = df['TimeCreated'].apply(is_suspicious)
suspicious = df[df['is_suspicious']]

print("⚠️ Suspicious Logins (Windows):\n")
for _, row in suspicious.iterrows():
    time = row['TimeCreated'].strftime('%Y-%m-%d %H:%M:%S')
    user = row['User']
    print(f"{time} - {user}")
    popup_alert(f"User '{user}' logged in at {time}.")
