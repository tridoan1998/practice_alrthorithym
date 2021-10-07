import smtplib
username = 'tri.doan@sjsu.edu'
password = '123456'
def send_mail(text="Email Body", subject="Hello World", from_email  = "tri.doan@sjsu.edu" to_emails=[]):
    assert isinstance(to_emails, list)
    server = smtplib.SMTP()
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail()

    server.quit()
    

