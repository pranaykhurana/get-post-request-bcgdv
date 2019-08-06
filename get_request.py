import requests
import json

URL = "https://interns.bcgdvsydney.com/api/v1/key"

reply = requests.get(URL)

print(reply.json())
print(type(reply.json()))

with open('C:/User/Pranay/Desktop/key.json', 'w') as ifile:
    json.dump(reply.json(), ifile)