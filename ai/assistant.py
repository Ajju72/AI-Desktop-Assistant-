import os

from dotenv import load_dotenv

from ai.gemini_client import GeminiClient

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

gemini = GeminiClient(API_KEY)

def process_query(user_text):
    return gemini.ask(user_text)
from automation.open_apps import open_application

def process_query(text):

    text = text.lower()

    if "open" in text:
        return open_application(text)

    return gemini.ask(text)
