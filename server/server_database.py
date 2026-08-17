import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).parent / "server.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            updated_at REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_note(note):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR REPLACE INTO notes
        (id, title, content, updated_at)
        VALUES (?, ?, ?, ?)
    """, (
        note["id"],
        note["title"],
        note["content"],
        note["updated_at"]
    ))

    connection.commit()
    connection.close()  