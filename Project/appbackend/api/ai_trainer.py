import openai

class AITrainer:
    def _init_(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def generate_notes(self, text):
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"Generate notes based on the following text:\n\n{text}",
            max_tokens=500
        )
        return response.choices[0].text.strip()

    def generate_quiz(self, text):
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"Generate a quiz based on the following text:\n\n{text}",
            max_tokens=500
        )
        return response.choices[0].text.strip()