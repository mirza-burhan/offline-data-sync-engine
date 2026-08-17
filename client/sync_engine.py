import requests

from database import get_unsynced_notes, mark_as_synced


SERVER_URL = "http://127.0.0.1:5000"


def send_note(note):
    try:
        response = requests.post(
            f"{SERVER_URL}/notes",
            json={
                "id": note[0],
                "title": note[1],
                "content": note[2],
                "updated_at": note[3]
            },
            timeout=5
        )

        return response

    except requests.RequestException:
        return None


def sync_notes():
    notes = get_unsynced_notes()

    if not notes:
        print("No notes to synchronize.")
        return

    print(f"Found {len(notes)} unsynchronized note(s).")

    for note in notes:
        print(f"Syncing note {note[0]}...")

        response = send_note(note)

        if response is not None and response.status_code == 201:
            mark_as_synced(note[0])
            print(f"Note {note[0]} synchronized successfully.")
        else:
            print(f"Note {note[0]} could not be synchronized.")


if __name__ == "__main__":
    sync_notes()