import sqlite3
from pathlib import Path
import time


DB_PATH = Path(__file__).parent.parent / "data" / "local.db"


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            updated_at REAL NOT NULL,
            synced INTEGER DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()

def add_note(title, content):
    connection = get_connection()
    cursor = connection.cursor()

    timestamp = time.time()

    cursor.execute("""
        INSERT INTO notes (title, content, updated_at, synced)
        VALUES (?, ?, ?, 0)
    """, (title, content, timestamp))

    connection.commit()
    connection.close()
def get_notes():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, content, updated_at, synced
        FROM notes
    """)

    notes = cursor.fetchall()

    connection.close()

    return notes
def get_unsynced_notes():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, content, updated_at, synced
        FROM notes
        WHERE synced = 0
    """)

    notes = cursor.fetchall()

    connection.close()

    return notes
def mark_as_synced(note_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE notes
        SET synced = 1
        WHERE id = ?
    """, (note_id,))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()

    notes = get_unsynced_notes()

    print("Unsynced notes:")

    for note in notes:
        print(note)