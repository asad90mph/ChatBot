from flask import Flask, request, jsonify
import openai
class ChatGPTBot:
    def __init__(self, api_key, engine="text-davinci-002"):
        self.api_key = api_key
        self.engine = engine
        self.prompts = []

    def initialize_gpt3(self):
        openai.api_key = self.api_key

    def create_prompt(self, prompt):
        self.prompts.append(prompt)
        return len(self.prompts) - 1

    def get_response(self, prompt_index):
        if prompt_index < 0 or prompt_index >= len(self.prompts):
            return "Invalid prompt index."
        prompt = self.prompts[prompt_index]
        response = openai.Completion.create(engine=self.engine, prompt=prompt, max_tokens=3000,  # Set maximum tokens to accommodate larger responses
        temperature=0.7,  # Adjust the temperature as needed
        n=1,  # Generate only one response
        stream=False ) # Get the full response without truncation)
        return response["choices"][0]["text"].strip()

    def update_prompt(self, prompt_index, new_prompt):
        if prompt_index < 0 or prompt_index >= len(self.prompts):
            return "Invalid prompt index."
        self.prompts[prompt_index] = new_prompt
        return "Prompt updated successfully."

app = Flask(__name__)
bot = None  # Initialize bot instance

@app.route('/initialize', methods=['POST'])
def initialize():
    global bot
    api_key = request.json.get('api_key')
    bot = ChatGPTBot(api_key)
    bot.initialize_gpt3()
    return "ChatGPT Bot initialized successfully."

@app.route('/create_prompt', methods=['POST'])
def create_prompt():
    prompt = request.json.get('prompt')
    if not prompt:
        return "Please provide a valid prompt."
    prompt_index = bot.create_prompt(prompt)
    return jsonify({"prompt_index": prompt_index})

@app.route('/get_response', methods=['POST'])
def get_response():
    prompt_index = request.json.get('prompt_index')
    if prompt_index is None:
        return "Please provide a valid prompt index."
    response = bot.get_response(prompt_index)
    return jsonify({"response": response})

@app.route('/update_prompt', methods=['POST'])
def update_prompt():
    prompt_index = request.json.get('prompt_index')
    new_prompt = request.json.get('new_prompt')
    if prompt_index is None or not new_prompt:
        return "Please provide a valid prompt index and new prompt."
    result = bot.update_prompt(prompt_index, new_prompt)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)