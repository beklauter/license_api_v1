import os

from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()
print()
app = Flask(__name__)

licenses = {
    "license1": True,
    "license2": False,
    "license3": True
}

@app.route('/license/<license_name>', methods=['GET'])
def check_license(license_name):
    status = licenses.get(license_name)
    if status is None:
        return jsonify({"error": "Lizenz nicht gefunden"}), 404
    return jsonify({"license": license_name, "activated": status}), 200

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG"), host=os.getenv("HOST"), port=os.getenv("PORT"))

