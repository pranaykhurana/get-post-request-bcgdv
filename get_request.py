# importing the required libraries
import requests
import json

#assigning the variable with the url of api
URL = "https://interns.bcgdvsydney.com/api/v1/key"

#making a get request and storing the contents
reply = requests.get(URL)

#printing the received contents 
print(reply.json())

#writing the received contents
with open('C:/User/Pranay/Desktop/key.json', 'w') as ifile:
    json.dump(reply.json(), ifile)