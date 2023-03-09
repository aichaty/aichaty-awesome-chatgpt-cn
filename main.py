# -*- coding: utf-8 -*-
import openai
openai.api_key = "sk-XXXXXXXXXXXXXXXXXXXX"  # 你的 OpenAI API Key

def completion(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    message = response.choices[0].message.content
    return message
print(completion(input("向ChatGPT提问：")))