from flask import Flask, request, jsonify
import random

app = Flask(__name__)

user_logins = dict()

@app.route("/register_user", methods=["POST"])
def handle_register_user():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "POST body could not be parsed as json"}), 400
    if "username" not in data:
        return jsonify({"error": "request has no username"}), 400
    if "password" not in data:
        return jsonify({"error": "request has no password"}), 400
    
    key = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(8))

    user_logins[data["username"]] = {
        "password" : data["password"],
        "key" : key
    }

    return jsonify({"message": "Account created successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
