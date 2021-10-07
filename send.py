from datetime import datetime
import requests
import sys
from formatting import format_mes

def send(name, website=None, verbose = False):
    if website != None:
        msg = format_mes(myname=name, mywebsite=website)
    else:
        msg = format_mes(myname=name)
    r = requests.get("http://httpbin.org/json")
    if verbose:
        print(name, website)
    if r.status_code== 200:
        print(r.json())
    else:
        return "there is an error"
    return msg


if __name__="__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
        
    response = send("Tri", "webside", verbose=True)
    print(response)
