import requests
import os
import random
import json
import string


chars = string.ascii_letters + string.digits + "!@#$%^&*()"
random.seed = (os.urandom(1024))

url = 'http://localhost/stealdata.php'

passlnght = list(range(8, 17))
emdigitlnght = [0,1,2,3]
domains = ["@yahoo.com", "@yahoo.co.uk", "@gmail.com", "@googlemail.com", "@outlook.com"]

names = json.loads(open("names.json").read())

for name in names:
    name_extra = ''.join(random.choice(string.digits) for i in range(random.choice(emdigitlnght)))

    username = name.lower() + name_extra + random.choice(domains)
    password = ''.join(random.choice(chars) for i in range(random.choice(passlnght)))

    requests.post(url, allow_redirects=False, data={
        "inputEmailHandle" : username,
        "inputPassword" : password
    })

    print ('sending username %s and password %s'%(username, password))
