import os
import openai
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()

def get_openai_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key not found. Make sure it is set in the environment.")
    return api_key

def make_chat_completion_request():
    openai.api_key = get_openai_api_key()

    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello world"}]
    )

    return chat_completion

def run_chat_completion():
    # Make API call
    chat_completion_result = make_chat_completion_request()
    return chat_completion_result

if __name__ == "__main__":
    chat_completion_result = run_chat_completion()
    print(chat_completion_result)
