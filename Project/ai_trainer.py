from g4f.client import Client

class AITrainer:
    client = None

    @classmethod
    def configure_api_key(cls, api_key):
        cls.client = Client(api_key=api_key)

    @classmethod
    def generate_notes(cls, text):
        if cls.client is None:
            raise ValueError("API client is not configured. Please call configure_api_key() first.")
        response = cls.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}]
        )
        return response.choices[0].message.content

    @classmethod
    def generate_quiz(cls, text):
        if cls.client is None:
            raise ValueError("API client is not configured. Please call configure_api_key() first.")
        response = cls.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Create a quiz for the following content: {text}"}]
        )
        return response.choices[0].message.content