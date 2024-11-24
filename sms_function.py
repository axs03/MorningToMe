import smtplib
from email.message import EmailMessage
from ssl import create_default_context


class SMS():
    def __init__(self, send_from: str, sender_pwd: str, send_to: str, subject="", body=""):
        self.send_from = send_from
        self.send_to = send_to
        self.sender_pwd = sender_pwd
        self.subject = subject
        self.body = body


    def newSMS(self) -> bool:
        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = self.send_from
        msg['To'] = self.send_to
        msg.set_content(self.body)

        try:
            with smtplib.SMTP('smtp.mail.yahoo.com', 587) as server: 
                server.starttls()
                server.login(self.send_from, self.sender_pwd)
                server.send_message(msg)
            return True

        except smtplib.SMTPException as e:
            print(f"Text Sending has failed: {e}")
            return False