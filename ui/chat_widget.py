from PyQt6.QtWidgets import QTextEdit

class ChatWidget(QTextEdit):
    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

    def add_user_message(self, text):
        self.append(f"You: {text}")

    def add_ai_message(self, text):
        self.append(f"Assistant: {text}")
