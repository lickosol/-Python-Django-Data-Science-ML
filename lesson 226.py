from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

html_templates = Template(Path('templates/index.html').read_text())

html_content = html_templates.substitute({'name': input("Введите имя: ")})

my_email = EmailMessage()
my_email['from'] = 'Lesya'
my_email['to'] = 'agentsoldat817@gmail.com'
my_email['subject'] = "Let's go out!"
my_email.set_content(html_content, 'html')

with open('images/empty.jpeg', 'rb') as img:
    image_data = img.read()
    my_email.add_attachment(image_data, maintype='image', subtype='jpeg', filename='empty.jpeg')

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    smtp_server.send_message(my_email)
    print('Email was sent!')