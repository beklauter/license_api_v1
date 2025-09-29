import os
import user
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/license/<license_key>', methods=['GET'])
def check_license(license_key):
    api_key = request.headers.get('X-API-Key') or request.args.get('api_key')

    license_found = False
    license_data = None
    license_username = None

    for username, user_obj in user.users.items():
        for license_obj in user_obj.licenses:
            if license_obj["license_key"] == license_key:
                license_found = True
                license_data = license_obj
                license_username = username
                break
        if license_found:
            break

    if not license_found:
        return jsonify({"error": "Lizenz nicht gefunden"}), 404

    if api_key and api_key != license_data["api_key"]:
        return jsonify({"error": "API-Key stimmt nicht mit der Lizenz überein"}), 403

    return jsonify({
        "license": license_key,
        "activated": license_data["activated"],
        "user": license_username,
        "api_key": license_data["api_key"]
    }), 200

def api_run():
    app.run(debug=os.getenv("DEBUG") == "True",
            host=os.getenv("HOST"),
            port=int(os.getenv("PORT")))