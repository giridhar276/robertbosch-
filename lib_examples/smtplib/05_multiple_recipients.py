import smtplib
recipients = ["a@example.com", "b@example.com", "c@example.com"]
message = "Subject: Team Update\n\nHello team, here is the update."
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_app_password")
server.sendmail("your_email@gmail.com", recipients, message)
server.quit()
