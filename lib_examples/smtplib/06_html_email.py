import smtplib
from email.mime.text import MIMEText
html_content = "<h1>Hello</h1><p>This is an <b>HTML</b> email.</p>"
msg = MIMEText(html_content, "html")
msg["Subject"] = "HTML Email"
msg["From"] = "your_email@gmail.com"
msg["To"] = "receiver@example.com"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_app_password")
server.send_message(msg)
server.quit()
