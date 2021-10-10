#Open inbox
import imaplib
import email

host = 'imap.gmail.com'
username = 'tri.doan@sjsu.edu'
password = '123456'

mail = imaplib.IMAP4_SSL(host)
mail.login(username, password)
mail.select("inbox")

_, search_data = mail.search(None, 'UNSEEN')

for num in search_data[0].split():
    print(num)
    _, data = mail.fetch(num, '(RFC822)')
    print(data)
