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

   git clone https://github.com/yourusername/chatbot-project.git

2. Navigate to the project directory:

   cd chatbot-project

3. Create a virtual environment:

   python -m venv venv

4. Activate the virtual environment:

   - **Windows**:
     venv\Scripts\activate
   - **Mac/Linux**:
     source venv/bin/activate

5. Install dependencies:

   pip install -r requirements.txt

6. Create a `.env` file in the project root and add your OpenAI API key:

   OPENAI_API_KEY=your-openai-api-key-here

7. Run the chatbot:

   python chatbot.py

## OpenAI API Key

To obtain an API key, sign up at [OpenAI](https://platform.openai.com/).
