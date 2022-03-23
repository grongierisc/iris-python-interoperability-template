import grongier.pex
import smtplib
from email.mime.text import MIMEText

class EmailOperation(grongier.pex.BusinessOperation):

    def OnMessage(self, pRequest):

        sender = 'admin@example.com'
        receivers = [ pRequest.ToEmailAddress ]


        port = 1025
        msg = MIMEText('This is test mail')

        msg['Subject'] = pRequest.Found+" found"
        msg['From'] = 'admin@example.com'
        msg['To'] = pRequest.ToEmailAddress

        with smtplib.SMTP('localhost', port) as server:
            
            # server.login('username', 'password')
            server.sendmail(sender, receivers, msg.as_string())
            print("Successfully sent email")
