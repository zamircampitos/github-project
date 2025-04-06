import requests
import json

url = "https://api.example.com/data"
data = {
  "name": "John Doe",
  "age": 30,
  "city": "New York"
}

response = requests.post(url, data=json.dumps(data))

if response.status_code == 201:
    print("Data successfully posted!")
else:
    print(f"An error occurred: {response.status_code} - {response.text}")
