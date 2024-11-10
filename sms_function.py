from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

load_dotenv()

sender_email, to_email = os.getenv("email"), os.getenv("to_email")
sender_pwd = os.getenv("email_passwd")

subject, mailtext = "", ""

msg=EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = to_email  
msg.set_content(mailtext)

def sendText() -> None:
    with smtplib.SMTP('smtp.gmail.com', 587) as server: 
        server.starttls()
        server.login(sender_email, sender_pwd)
        server.send_message(msg)