import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "sivm0987@gmail.com"
sender_password = "bcjj fxjx ucuw dney"  # Use the app password generated from Google

# List of recipients
recipients = [
    "freefireshivam0987@gmail.com",
]

# Email content
subject = "Test Email"
body = """
Hello,

This is a test email sent to multiple recipients using Python.

Best regards,
Your God: Shivam
"""

# Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Set up the SMTP server and send the email
try:
    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)

    # Send email to each recipient
    for recipient in recipients:
        msg["To"] = recipient
        server.sendmail(sender_email, recipient, msg.as_string())

    print("Emails sent successfully!")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
finally:
    server.quit()
