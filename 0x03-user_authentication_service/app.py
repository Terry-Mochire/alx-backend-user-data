#!/usr/bin/env python3

"""
Flask app
"""

from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
Auth = Auth()


@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
