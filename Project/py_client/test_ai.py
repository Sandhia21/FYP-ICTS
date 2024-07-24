import sys
import os

# Adjust the path to include the root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from ai_trainer import AITrainer

def test_generate_notes():
    text = "The process of photosynthesis involves the conversion of light energy into chemical energy by plants."
    notes = AITrainer.generate_notes(text)

    print("Generated Notes:")
    print(notes)

def test_generate_quiz():
    text = "The process of photosynthesis involves the conversion of light energy into chemical energy by plants."
    quiz = AITrainer.generate_quiz(text)

    print("Generated Quiz:")
    print(quiz)

if __name__ == "__main__":
    AITrainer.configure_api_key()  # Configure the API client
    test_generate_notes()
    test_generate_quiz()