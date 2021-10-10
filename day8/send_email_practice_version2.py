

import smtplib, ssl
smtp_server= "stmp.gmail.com"
port = 587
sender_email = "tri.doan@sjsu.edu"
receiver_email = "tridoan1998@gmail.com"
password = input("Please enter your password and press enter: ")
message = """\
Subject: Hi there 

This message is sent from Python.
"""
context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
except Exception as e:
    print(e)
finally:
    server.quit()