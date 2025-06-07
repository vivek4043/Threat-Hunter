import smtplib
from email.message import EmailMessage

def send_alert(subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'receiver_email@gmail.com'
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your_email@gmail.com', 'your_app_password')
        smtp.send_message(msg)
