import requests
import json
from api_key_personal import api


def model_list():
    list = {1: "gpt-3.5-turbo", 2: "gpt-4", 3: "text-davinci-003"}
    return list


model = model_list()[2]

# Set the endpoint URL
url = "https://api.openai.com/v1/chat/completions"

model_url = f"https://api.openai.com/v1/models/{model}"

# Set the headers
headers_request = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api()}"
}

# Set the payload (JSON data)
payload = {
    "model": model,
    "messages": [{"role": "user", "content": "say this is a test!"}],
    "n": 1
}

# Send the POST request
response = requests.post(url, headers=headers_request, json=payload)
# Get the response JSON data
json_data = response.json()

# Send the GET request to Retrieve model basic information
model_get = requests.get(model_url, headers=headers_request)
json_data2 = model_get.json()


formatted_data = json.dumps(json_data, indent=4)
formatted_data2 = json.dumps(json_data2, indent=4)
print(formatted_data + "\n" + formatted_data2)
