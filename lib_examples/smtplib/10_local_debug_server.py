import smtplib
# For local testing, run: python -m smtpd -c DebuggingServer -n localhost:1025
server = smtplib.SMTP("localhost", 1025)
server.sendmail("test@example.com", "receiver@example.com", "Subject: Local Test\n\nTesting locally")
server.quit()
