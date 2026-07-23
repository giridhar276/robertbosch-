import smtplib
import ssl
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login("your_email@gmail.com", "your_app_password")
    server.sendmail("your_email@gmail.com", "receiver@example.com", "Subject: SSL Test\n\nSecure email")
