import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Stephen Axtell'
email['to'] = 'axtell.stephen@gmail.com'
email['subject'] = 'Greetings from Switzerland'

email.set_content(html.substitute(name='Leeroy'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<your email username>', '<your email password>')
    smtp.send_message(email)
    print('Done and dusted')
