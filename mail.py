# import smtplib
# a = 'sdsjdjsdjjd'
# smtpobj = smtplib.SMTP('smtp.yandex.ru', 587)
# smtpobj.starttls()
# smtpobj.login('zabbix-VM@yandex.ru', 'VM$2019')
# smtpobj.sendmail("zabbix-VM@yandex.ru", "jar1991@mail.ru", "test")
# smtpobj.quit()

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object
msg = MIMEMultipart()

message = "test text"

# setup the parameters of the message
password = "VM$2019"
msg['From'] = "zabbix-VM@yandex.ru"
msg['To'] = "jar1991@mail.ru"
msg['Subject'] = "Subscription"

# add in the message body

msg.attach(MIMEText(message, 'plain'))

# create server
server = smtplib.SMTP('smtp.yandex.ru: 465')

server.starttls()

# login credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print ("succesfully sent email to %s:" % (msg['To']))