from datetime import datetime
import requests
import sys
from formatting import format_mes
from send_mail import send_mail

def send(name, website=None, to_email= None, verbose = False):
    assert to_email != None
    if website != None:
        msg = format_mes(myname=name, mywebsite=website)
    else:
        msg = format_mes(myname=name)
    r = requests.get("http://httpbin.org/json")
    if verbose:
        print(name, website, to_email)
    #send the message
    try:
        send_mail(text=msg,to_email=[to_email], html=None)
        sent = True
    except:
        sent = False
    return sent

if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    email = None
    if len(sys.argv) > 2 :
        email = sys.argv[2]

        
    response = send(name, to_email= email, verbose=True)
    print(response)
