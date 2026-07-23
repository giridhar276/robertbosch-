import smtplib
try:
    server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
    server.starttls()
    server.login("your_email@gmail.com", "wrong_password")
except smtplib.SMTPAuthenticationError as e:
    print("Authentication failed:", e)
except smtplib.SMTPException as e:
    print("SMTP error:", e)
finally:
    server.quit()
