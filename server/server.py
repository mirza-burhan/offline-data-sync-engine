from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Offline Data Sync Server is running!"


@app.route("/notes", methods=["POST"])
def create_note():
    note = request.get_json()

    print("Received note:", note)

    return jsonify({
        "message": "Note received successfully",
        "note": note
    }), 201


if __name__ == "__main__":
    app.run(debug=True)