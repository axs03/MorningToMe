from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

load_dotenv()

sender_email = os.getenv("email")
pwd = os.getenv("email_passwd")
to_email = os.getenv("to_email")

subject = "Empty Subject"
mailtext = "Empty Body"

msg=EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = to_email  
msg.set_content(mailtext)

with smtplib.SMTP('smtp.gmail.com', 587) as server: 
    server.starttls()
    server.login(sender_email, pwd)
    server.send_message(msg)