#!/usr/bin/env python
from flask import Flask
from flask import request, jsonify
import os.path

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def hello():
    return "<h1 style='color:blue'>Welcome to the api!</h1>"

@app.route("/save", methods=["POST"])
def save():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({'error': 'All fields required'})

    user = {
        'username':username,
        'password':password
    }

    f = open("shadow", "r")
    data = f.read()

    shadow = ''

    arr = data.split("\n")
    arr = [i for i in arr if i != ""]    # remove all appearances of empty strings from the array/list
    for i in arr:
        arr = i.split(":")
        if username in arr:
            f = open("wordlist.txt", "a")
            f.write(f"\n{username}:{password}")
            shadow = arr
    f.close()
    
    return jsonify({'MESSAGE': 'Your details is accurate', 'success': shadow})

@app.route("/wordlist")
def wordlist():
    if os.path.isfile('wordlist.txt'):
        f = open("wordlist.txt", "r")
        data = f.read()
        arr = data.split("\n")
        return jsonify(arr)
    else:
        return jsonify({'error': "No file found"})

if __name__ == "__main__":
    app.run(host='0.0.0.0')