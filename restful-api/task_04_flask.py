#!/usr/bin/env python3
"""
    Module to showcase a basic flask server
"""


from flask import Flask, jsonify, request


users_dict = {}

app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users_dict))

@app.route("/status")
def status():
    return "Ok"

@app.route("/users/<username>")
def list_user(username):
    if username is None:
        return jsonify({'error': 'Username is required'}), 400

    if username not in users_dict:
        return jsonify({'error': 'User not found'}), 401

    return jsonify(users_dict[username])


@app.route('/add_user', methods=['POST'])
def add_user():
    # inbound data: "username": "john", "name": "John", "age": 30, "city": "New York"
    body = request.json
    if body is None or body.get('username') is None:
        return jsonify({'error': 'Username is required'}), 400

    if body.get('username') in users_dict:
        return jsonify({"error":"Username already exists"}), 409

    try:
        user = {
        'username': body.get('username'),
        'name': body.get('name'),
        'age': body.get('age'),
        'city': body.get('city')
        }
        users_dict[body.get('username')] = user
    except:
        return jsonify({'error': 'Invalid JSON'}), 400

    return jsonify({"message": "User added", "user": user}), 201

if __name__ == '__main__':
    app.run()
