import os
import sys
import openai
from openai import OpenAI

client = OpenAI(
    api_key = os.getenv("APIKEY")
)

def get_user_input(prompt="You: "):
    return input(prompt)

def generate_response(messages, model = "gpt-4o-mini", max_tokens = 1000, temperature = 0.7):
    response = client.chat.completions.create(
        model = model,
        messages = messages,
        max_tokens = max_tokens,
        temperature = temperature
    )
    return response.choices[0].message.content

def main():
    #api_key = get_api_key()
    #client = initialize_api_key(api_key)
    
    #print("Welcome to the Chatbot!, Type 'exit' to end the conversation.\n")

    messages = [
        {"role": "system", "content": "You are a chatbot for now"}
    ]
    while True:
        user_input = get_user_input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Exiting Chat..")
            break

        messages.append({"role": "user", "content": user_input})
        
        bot_response = generate_response(messages)
        print(f"Bot: {bot_response}\n")

        messages.append({"role": "assistant", "content": bot_response})

if __name__ == "__main__":
    main()