from flask import request, jsonify

class User:
    def signup(self):
        user = {
            "_id": "",
            "username": "",
            "email": "",
            "password": ""
        }

        return jsonify(user), 200