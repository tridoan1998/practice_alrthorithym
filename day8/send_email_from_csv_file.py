import smtplib, ssl

import csv
with open("contact_file.csv") as file:
    reader= csv.reader(file)
    next(reader)
    for name, email, grade in reader:
        print(f"Senfing email to {name}")

sender_email = "tri.doan@sjsu.edu"
receive_email = "tridoan1998@gmail.com"
password = input("Please enter password")

context =