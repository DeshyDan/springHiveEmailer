from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import random

from email.header import Header
from email.mime.text import MIMEText
#Open a file for reading

me = 'deshy733@gmail.com' # change to your email
p_reader = open('password.txt', 'rb') # edit for your password
cipher = p_reader.read()
recipients = ['SomeEMailHEre'] # enter recipients here


def spamEveryMinute():
    while (True):
        msg = MIMEMultipart()
        msg['From'] = me
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = Header('BTR Giveaway 2024', 'utf-8')

        # Attach the message body
        fp = open('message.txt', 'rb')
        body = MIMEText(fp.read(), 'plain', 'utf-8')
        fp.close()
        msg.attach(body)

        # Attach the PDF file
        filename = 'Resume.pdf'
        attachment = open(filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)
        msg.attach(part)

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(me, cipher.decode('utf-8'))
        s.sendmail(me, recipients, msg.as_string())

        print("Email sent to: " + ', '.join(recipients))
        s.quit()
        time.sleep(60) # change rate of fire here

spamEveryMinute()