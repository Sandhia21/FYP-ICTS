from g4f.client import Client

class AITrainer:
    client = None

    @classmethod
    def configure_api_key(cls, api_key=None):
        cls.client = Client()

    @classmethod
    def generate_notes(cls, text):
        if not cls.client:
            raise ValueError("API client is not configured. Please call configure_api_key() first.")
        
        try:
            response = cls.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Generate notes based on the following text:\n\n{text}"}
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"

    @classmethod
    def generate_quiz(cls, text):
        if not cls.client:
            raise ValueError("API client is not configured. Please call configure_api_key() first.")
        
        try:
            response = cls.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": f"Generate a quiz based on the following text:\n\n{text}"}
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"