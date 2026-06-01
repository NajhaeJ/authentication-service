from flask import Flask, request, jsonify
import random

app = Flask(__name__)

user_logins = dict()

def validate_auth_request(req):
    data = req.get_json(silent=True)
    if not data:
        return None, ("POST body could not be parsed as json", 400)
    if "username" not in data:
        return None, ("request has no username", 400)
    if "password" not in data:
        return None, ("request has no password", 400)
    
    return data, None

@app.route("/register_user", methods=["POST"])
def handle_register_user():
    data, error = validate_auth_request(request)
    if error:
        error_message, status_code = error
        return jsonify({"error": error_message}), status_code
    
    
    key = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for i in range(8))

    user_logins[data["username"]] = {
        "password" : data["password"],
        "key" : key
    }

    return jsonify({"message": "Account created successfully"}), 200

@app.route("/login_user", methods=["POST"])
def handle_login_user():
    data, error = validate_auth_request(request)
    if error:
        error_message, status_code = error
        return jsonify({"error": error_message}), status_code

    if data["username"] not in user_logins:
        return jsonify({"error": "username not found"}), 404

    if user_logins[data["username"]]["password"] != data["password"]:
        return jsonify({"error": "password incorrect"}), 401
    

    return jsonify({"message": "Login successful"}), 200

if __name__ == '__main__':
    app.run(debug=True)
