import openai
from api_key_personal import api

openai.api_key = api()

# chat_hello = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(openai.Model.retrieve("gpt-3.5-turbo-16k-0613"))

