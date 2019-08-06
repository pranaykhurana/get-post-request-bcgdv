import requests

url = "https://interns.bcgdvsydney.com/api/v1/submit"

apiKey = {"apiKey":"ab5623f9-9596-41ab-a556-fa912804407f"}

payload = "{\"name\": \"Pranay Khurana\",\"email\": \"pranay.khurana99@gmail.com\"\t}"

response = requests.request("POST", url, data=payload, params=apiKey)

print(response.text)
print(response)
print(response.json())