import smtplib
from email.mime.text import MIMEText
msg = MIMEText("This is the body of the email")
msg["Subject"] = "Test Email"
msg["From"] = "your_email@gmail.com"
msg["To"] = "receiver@example.com"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_app_password")
server.send_message(msg)
server.quit()
