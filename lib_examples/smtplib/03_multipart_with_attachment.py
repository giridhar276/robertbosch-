import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

msg = MIMEMultipart()
msg["Subject"] = "Report Attached"
msg["From"] = "your_email@gmail.com"
msg["To"] = "receiver@example.com"
msg.attach(MIMEText("Please find the attached report.", "plain"))
with open("report.pdf", "rb") as f:
    part = MIMEApplication(f.read(), Name="report.pdf")
    msg.attach(part)

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_app_password")
server.send_message(msg)
server.quit()
