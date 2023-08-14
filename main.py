### Code from openai

import openai

class ChatGPTPlugin:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_response(self, prompt):
        response = openai.Completion.create(
            engine="davinci",  # Use the appropriate GPT-3 engine
            prompt=prompt,
            max_tokens=50  # Adjust the response length as needed
        )
        return response.choices[0].text.strip()

# Replace 'YOUR_API_KEY' with your actual GPT-3 API key
plugin = ChatGPTPlugin(api_key='YOUR_API_KEY')

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = plugin.generate_response(user_input)
    print("Bot:", response)