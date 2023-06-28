import openai
from api_key_personal import api

openai.api_key = api()
length_limit = 18
whatModel = "gpt-3.5-turbo"
question = "what makes AI so useful? short answer!"

# print(openai.Model.retrieve("gpt-3.5-turbo"))

responses = openai.ChatCompletion.create(
    temperature=1,
    n=1,
    max_tokens=length_limit,
    model=whatModel,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": question}
    ]
)

print(responses)

# print(completion.choices[0].message)
# or
print(responses['choices'][0]['message']['content'])

finish_reason = responses['choices'][0]['finish_reason']
if finish_reason == "stop":
    print("done")
elif finish_reason == "length":
    print("Length Limit! please adjust the value")
