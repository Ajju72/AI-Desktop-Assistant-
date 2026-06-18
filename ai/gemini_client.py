import google.generativeai as genai

class GeminiClient:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-1.5-flash"
        )

    def ask(self, prompt):
        try:
            response = self.model.generate_content(
                prompt
            )

            return response.text

        except Exception as e:
            return f"Error: {str(e)}"
