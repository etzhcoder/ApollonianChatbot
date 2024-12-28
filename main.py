import os
import sys
import openai


def get_api_key():
    api_key = os.getenv("APIKEY")
    return api_key

def initialize_api_key(api_key):
    openai.api_key = api_key

def get_user_input(prompt="You: "):
    return input(prompt)

def generate_response(messages, model = "gpt-4", max_tokens = 150, temperature = 0.7):
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens = max_tokens,
        temperature = temperature
    )
    return response.choices[0].message['content'].strip()

def main():
    api_key = get_api_key()
    initialize_api_key(api_key)
    print(api_key)


if __name__ == "__main__":
    main()