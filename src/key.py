import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Who won the world cup in 2018?"}
    ]
)

print(response.choices[0].message.content)