from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Desktop Assistant")
        self.resize(900, 600)

        layout = QVBoxLayout()

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText(
            "Ask anything..."
        )

        self.send_button = QPushButton("Send")

        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)

        self.setLayout(layout)
