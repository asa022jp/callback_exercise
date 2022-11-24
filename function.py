import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'my_address@example.com'
TARGET_EMAIL = "something@something.lol"
PASSWORD = 'mypassword'

name = data['name']
phone = data['phone']
email = data['email']
address = data['address']

def send_mail():
    # set up the SMTP server
    s = smtplib.SMTP(host='example_host_address', port=example_port)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # Send the email:
    msg = MIMEMultipart()       # create a message

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=TARGET_EMAIL
    msg['Subject']= "very important email pls open"
    
    message = name + "\n" + phone + "\n" + email + "\n" + address
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()