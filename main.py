from ai.assistant import process_query
from voice.speech_to_text import listen
from voice.text_to_speech import speak
import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton
)

class AssistantUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Desktop Assistant")
        self.resize(800, 600)

        layout = QVBoxLayout()

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type your message...")

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)

        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def send_message(self):
        message = self.input_box.text()

        if message:
            self.chat_area.append(f"You: {message}")
            self.chat_area.append("Assistant: Processing...")
            self.input_box.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = AssistantUI()
    window.show()

    sys.exit(app.exec())

def voice_input(self):
    text = listen()

    if text:
        self.input_box.setText(text)

def send_message(self):
    user_text = self.input_box.text()

    if not user_text:
        return

    self.chat_area.append(
        f"You: {user_text}"
    )

    response = process_query(user_text)

    self.chat_area.append(
        f"Assistant: {response}"
    )

    self.input_box.clear()

self.voice_button = QPushButton("🎤 Voice")
layout.addWidget(self.voice_button)

self.voice_button.clicked.connect(
    self.voice_input
)
