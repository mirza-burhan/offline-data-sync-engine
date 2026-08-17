from flask import Flask, request, jsonify

from server_database import initialize_database, save_note


app = Flask(__name__)


@app.route("/")
def home():
    return "Offline Data Sync Server is running!"


@app.route("/notes", methods=["POST"])
def create_note():
    note = request.get_json()

    result = save_note(note)

    print(f"Received note {note['id']}: {result}")

    return jsonify({
        "message": "Note processed successfully",
        "result": result,
        "note": note
    }), 201


initialize_database()


if __name__ == "__main__":
    app.run(debug=True)