# -*- coding: utf-8 -*-
# Developer: Xianglin Wu (xianglin3092@gmail.com)
import _Email

sender_address = 'xxxxxxxx@gmail.com'
sender_passwords = 'xxxxxxxxxxxxxxxx'
receiver_address = 'xxxxxxxx@gmail.com'
subject= "Test subject"
content = '''Hello!
This is a test.
I'm attaching the two images in this email.
'''
image = ["star.png", "photo.jpg"]

flag = _Email.send_mail(sender_address, sender_passwords, receiver_address, subject, content, image)
print(flag)
