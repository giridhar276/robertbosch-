import smtplib
# Basic connection and sending a plain email
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_app_password")
server.sendmail("your_email@gmail.com", "receiver@example.com", "Subject: Hi\n\nHello there!")
server.quit()
