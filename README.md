# Embedding Llama Chatbot

Embedding Llama Chatbot is an application designed to help students learn university courses through an interactive chat interface. The application features a backend built with FastAPI and a frontend developed using Streamlit. This project is tested with Python 3.11.

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
- Integration with LLama model for natural language processing.

## Requirements
- Python 3.11
- LLama model

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/lucaslov/EmbeddingLlamaChatbot.git
    cd llama-chat-bot
    ```

2. (Optional) Create and activate a new environment using Conda:
    ```sh
    conda create --name llama-chat-bot python=3.11
    conda activate llama-chat-bot
    ```

3. Download the LLama model and place it in the root directory. You can use the following model as an example:
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
- `--temperature`: The temperature for the LlamaCPP model (default is `0.1`).
- `--model_path`: The path to the LlamaCPP model.

Example usage:
```sh
python main.py --pdf_file my_course.pdf --temperature 0.5 --model_path /path/to/your/model

