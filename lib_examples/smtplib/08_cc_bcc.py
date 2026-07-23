import smtplib
from email.mime.text import MIMEText
msg = MIMEText("Body with CC and BCC recipients")
msg["Subject"] = "CC BCC Test"
msg["From"] = "your_email@gmail.com"
msg["To"] = "primary@example.com"
msg["Cc"] = "cc_person@example.com"
all_recipients = ["primary@example.com", "cc_person@example.com", "bcc_person@example.com"]
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_app_password")
server.sendmail("your_email@gmail.com", all_recipients, msg.as_string())
server.quit()
