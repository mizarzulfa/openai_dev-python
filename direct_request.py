import requests
from api_key_personal import api

# Set the endpoint URL
url = "https://api.openai.com/v1/chat/completions"

# Set the headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api()}"
}

# Set the payload (JSON data)
payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 1
}

# Send the POST request
response = requests.post(url, headers=headers, json=payload)

# Get the response JSON data
data = response.json()

# Print the response
print(data)
