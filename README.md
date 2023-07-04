# template_openai

 The core of an app to use OpenAI's Language Model API. The code uses the OpenAI Python library and the dotenv package for environment variable management.

## Pre-requisites

To run the code in this repository, ensure you have the following:

- Python 3.x installed on your system
- An OpenAI API key, which you can get from openai.com


## Setup

- Clone the repo

    ```bash
    git clone
    ```

- Create a virtual environment

    ```bash
    python3 -m venv myenv
    ```

- Activate the virtual environment

    ```bash
    source venv/bin/activate
    ```

- Install the requirements

    ```bash
    pip install -r requirements.txt
    ```

- Create a .env file in the root directory and add the following

    ```bash
    OPENAI_API_KEY=<your_api_key>
    ```
- Run the app

    ```bash
    python3 app.py
    ```
- Open your browser and go to http://localhost:5000

## Docker

- Build the image

    ```bash
    docker build -t template_openai .
    ```
- Run the container

    ```bash
    docker run -d -p 5000:5000 template_openai
    ```
- Open your browser and go to http://localhost:5000


## Development

- Clone the repo
- Create a virtual environment

    ```bash
    python3 -m venv venv
    ```
- Activate the virtual environment

    ```bash
    source venv/bin/activate
    ```
- Install the requirements

    ```bash
    pip install -r requirements.txt
    ```
- Create a .env file in the root directory and add the following

    ```bash
    OPENAI_API_KEY=<your_api_key>
    ```
- Run the app

    ```bash
    python3 app.py
    ```

- Open your browser and go to <http://localhost:5000>

## Testing

- Clone the repo
- Create a virtual environment

    ```bash
    python3 -m venv venv
    ```
- Activate the virtual environment

    ```bash
    source venv/bin/activate
    ```
- Install the requirements

    ```bash
    pip install -r requirements.txt
    ```
- Create a .env file in the root directory and add the following

    ```bash
    OPENAI_API_KEY=<your_api_key>
    ```
- Run the tests

    ```bash
    pytest
    ```
- Open your browser and go to http://localhost:5000


## Installation
    
    ```bash
    pip install -r requirements.txt
    ```

## Usage

    ```bash
    python3 app.py
    ```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

