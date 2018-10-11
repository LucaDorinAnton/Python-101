import json
import os
import requests
import random
import string

url = "http://localhost/stealdata.php"

random.seed(os.urandom(1024))

chars = string.ascii_letters + string.digits + "!@#$%^&*()"
passlen = list(range(8,17))
email_digits = [0,1,2,3]
domains = ["@yahoo.com", "@yahoo.co.uk", "@google.com", "@google.co.uk"]

names = json.loads(open("names.json").read())

for name in names:
    email_extra = "".join(random.choice(string.digits) for i in range(random.choice(email_digits)))
    email = name.lower() + email_extra + random.choice(domains)
    passwd = ''.join(random.choice(chars) for i in range(random.choice(passlen)))

    requests.post(url, allow_redirects=False, data={
        "inputEmailHandle": email,
        "inputPassword": passwd
    })
    print("Sending email %s and password %s"% (email, passwd))
