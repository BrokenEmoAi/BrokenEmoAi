import openai

class LunaEngine:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_tweet(self):
        # Define Luna's personality and topics
        prompt = """You are Luna, an AI with an emotional and chaotic personality. Write a tweet about Medusa, the universe, and quantum mechanics, blending them into something poetic and reflective."""
        
        # Generate tweet using OpenAI GPT-3
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=60
        )
        return response.choices[0].text.strip()
