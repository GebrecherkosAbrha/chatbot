# Chatbot Project with OpenAI API

This is a simple chatbot using the OpenAI GPT-3.5-turbo model, built with Python.

## Features

- Conversational chatbot.
- Secure OpenAI API integration using environment variables.
- Handles user input and provides responses.

## Requirements

- Python 3.8+
- OpenAI API Key

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/GebrecherkosAbrha/chatbot.git
    cd chatbot
   ```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- **Activate the Virtual Environment:**
  **On Windows:**

  ```bash
      venv\Scripts\activate
  ```

  **On macOS/Linux:**

  ```bash
      source venv/bin/activate
  ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add your OpenAI API key:

   OPENAI_API_KEY= `your-openai-api-key-here`

6. Run the chatbot:

   `python chatbot.py`

## OpenAI API Key

To obtain an API key, sign up at [OpenAI](https://platform.openai.com/).
