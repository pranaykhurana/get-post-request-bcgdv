# importing the required libraries
import requests

#assigning the variable with the url of api
URL = "https://interns.bcgdvsydney.com/api/v1/submit"

#assigning the variable with the key received from get request
apiKey = {"apiKey":"00b6fd4c-4a48-43d5-9460-870957adb6a3"}

#assigning variable with name and email to be sent as payload
payload = "{\"name\": \"Pranay Khurana\",\"email\": \"pranay.khurana99@gmail.com\"\t}"

#making a post request
response = requests.request("POST", URL , data=payload, params=apiKey)

#printing the response
print(response.json())
print(response)