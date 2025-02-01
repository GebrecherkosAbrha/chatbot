import openai
import logging
from config import openai_api_key

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Set OpenAI API key
openai.api_key = openai_api_key


def chat_with_gpt(prompt):
    try:
        logging.info(f"User input: {prompt}")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response['choices'][0]['message']['content']
        logging.info(f"Chatbot response: {answer}")
        return answer
    except openai.error.OpenAIError as e:
        logging.error(f"Error: {e}")
        return f"Error: {e}"


def get_user_input():
    return input("You: ")


def main():
    print("Chatbot: Hello! Ask me anything. Type 'exit' to quit.")
    while True:
        user_input = get_user_input()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chat_with_gpt(user_input))


if __name__ == "__main__":
    main()
