# Embedding Llama Chatbot

Embedding Llama Chatbot is an application designed to help students learn university courses through an interactive chat interface. The application features a backend built with FastAPI that connects with Chroma and the Llama model, and a frontend UI developed using Streamlit. The chat interface leverages Chroma DB vector store to retrieve relevant information from PDF documents based on the user's query and passes it to the Llama large language model for response generation.

The application performs best on Apple M series processors, where the response time ranges from 30-40 seconds. On Windows computers, it cannot utilize the graphic card, resulting in a much slower response time of about 10 minutes.

#### Example Usage of the App
![Photo not available](https://github.com/lucaslov/EmbeddingLlamaChatbot/blob/main/docs/App%20Screen.png?raw=true)

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Features
- Interactive chat interface to aid in learning university courses.
- Backend powered by FastAPI.
- Frontend developed using Streamlit.
- Integration with Llama model for natural language processing.
- Integration with Chroma DB to retrieve relevant information from PDF documents.

## Requirements
- Python 3.11 or higher
- Llama model
- FastAPI
- Streamlit
- Chroma DB

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/lucaslov/EmbeddingLlamaChatbot.git
    cd EmbeddingLlamaChatbot
    ```

2. (Optional) Create and activate a new environment using Conda:
    ```sh
    conda create --name llama-chat-bot python=3.11
    conda activate llama-chat-bot
    ```
3. Download the Llama model and place it in the root directory. You can use the following model as an example:
    [LLama-2-13B-chat-GGUF](https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/blob/main/llama-2-13b-chat.Q2_K.gguf)

4. Modify the `--model` parameter in `run.py` to point to the path of the downloaded model:
    ```python
    --model /path/to/your/model
    ```

## Usage
To run the application, use the following command:
```sh
python run.py
```

## Configuration
The `main.py` file located in the background can take the following parameters:

- `--pdf_file`: The PDF file to load (default is `'ipb4.pdf'`).
- `--temperature`: The temperature for the Llama model (default is `0.1`).
- `--model_path`: The path to the Llama model.

Example usage:
```sh
python main.py --pdf_file my_course.pdf --temperature 0.5 --model_path /path/to/your/model
```

### Notes:
- Ensure that the paths to the model and PDF file are correct.
- Adjust the temperature parameter to fine-tune the response randomness and creativity as needed.