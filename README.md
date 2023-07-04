# template_openai

The core code to use OpenAI's Language Model API. The code uses the OpenAI Python library and the dotenv package for environment variable management.

## Pre-requisites

To run the code in this repository, ensure you have the following:

- Python 3.x installed on your system
- An OpenAI API key, which you can get from [OpenAI](https://openai.com).

## Setup

- Clone the repo

    ```bash
    git clone https://github.com/Sum1Solutions/template_openai.git
    ```

- Create a virtual environment

    ```bash
    python3 -m venv env
    ```

- Activate the virtual environment (so the required files don't mess with your own system's files)

    ```bash
    source venv/bin/activate
    ```

- Install the various libraries and modules this app requires

    ```bash
    pip install -r requirements.txt
    ```

- Create a .env file with your own secret key (i.e., your <your_api_key> from OpenAI)

    ```bash
   echo "OPENAI_API_KEY=<ReplaceThisPartWithYourAPI>" > .env
    ```

## Usage (via CLI)

```bash
    python3 app.py
```
-App.py is a command-line that connects to OpenAI and ensures the connection is functioning.
-App2.py is a command-line tool to prompt for information and returns data from the model.

```bash
    python3 app2.py
```

## Usage (via Browser)

App3.py is browser tool (of app2) that prompts for a question.

```bash
    python3 app3.py
 ```
- Open your browser and go to http://localhost:5000

