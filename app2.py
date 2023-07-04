import os
import openai
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()

def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found. Make sure it is set in the environment.")
    # Validate the format of the API key if needed
    # Add additional validation logic if necessary
    return api_key

def make_chat_completion_request(messages):
    openai.api_key = get_openai_api_key()

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return chat_completion

def run_chat_completion():
    messages = [{"role": "user", "content": "Hello world"}]  # Initialize with a user message
    termination_conditions = ["thank you", "bye", "quit"]  # Define termination conditions

    while True:
        user_input = input("User: ")
        messages.append({"role": "user", "content": user_input})

        if any(condition in user_input.lower() for condition in termination_conditions):
            break

        # Make API call
        chat_completion_result = make_chat_completion_request(messages)

        # Extract assistant response and process it if needed
        assistant_response = chat_completion_result["choices"][0]["message"]["content"]
        print("Assistant:", assistant_response)

        messages.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    run_chat_completion()
