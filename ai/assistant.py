from ai.gemini_client import GeminiClient

API_KEY = "API"

gemini = GeminiClient(API_KEY)

def process_query(user_text):
    return gemini.ask(user_text)
