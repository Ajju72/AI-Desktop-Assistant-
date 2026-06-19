import sqlite3

class DatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect(
            "chat_history.db"
        )

        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT,
            ai_response TEXT
        )
        """)

        self.conn.commit()

    def save_chat(
        self,
        user_message,
        ai_response
    ):
        self.cursor.execute(
            """
            INSERT INTO chats(
                user_message,
                ai_response
            )
            VALUES (?,?)
            """,
            (user_message, ai_response)
        )

        self.conn.commit()

    def get_chats(self):
        self.cursor.execute(
            "SELECT * FROM chats"
        )

        return self.cursor.fetchall()
