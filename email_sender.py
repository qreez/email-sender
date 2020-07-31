import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Qreez'
email['to'] = 'sendEmailTo@gmail.com'
email['subject'] = 'Type your email subject here'

email.set_content(html.substitute({'name': 'recipientNameHere'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('username@gmail.com', 'password')
    smtp.send_message(email)
    print('all done!')
