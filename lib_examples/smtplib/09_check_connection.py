import smtplib
server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
status = server.noop()
print("NOOP status:", status)
server.quit()
