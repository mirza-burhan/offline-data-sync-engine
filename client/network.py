import requests
import threading
import time

from sync_engine import sync_notes


SERVER_URL = "http://127.0.0.1:5000"


def is_online():
    try:
        requests.get(
            f"{SERVER_URL}/",
            timeout=3
        )
        return True
    except requests.RequestException:
        return False


def network_listener():
    was_online = is_online()

    while True:
        time.sleep(5)

        currently_online = is_online()

        if not was_online and currently_online:
            print("Network/server connection restored.")
            sync_notes()

        was_online = currently_online


if __name__ == "__main__":
    listener = threading.Thread(
        target=network_listener,
        daemon=True
    )

    listener.start()

    print("Network listener started.")

    while True:
        time.sleep(1)