# -*- coding: utf-8 -*-
# Developer: Xianglin Wu (xianglin3092@gmail.com)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path

def send_mail(sender_address, sender_passwords, receiver_address, subject, content, image=None):
    """
    You should use google app passwords as your sender_passwords.
    Please refer to the webside below,and mind whether you have turned on the 2-Step Verification or not.
    https://support.google.com/accounts/answer/185833?hl=en

     Input:
      sender_address: str
      sender_passwords: str
      receiver_address: str
      subject: str
      content: str
      **image: list of str
     Output:
      If no error exises ->  return True
      If errors exist  ->  return False
    """
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject   
    message.attach(MIMEText(content, 'plain'))    
    if image != None:
        for i in range(len(image)):
            message.attach(MIMEImage(Path(image[i]).read_bytes()))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    try:
        session.starttls()
        session.login(sender_address, sender_passwords)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        return True
    except Exception as e:
        print("Error message: ", e)
        return False
