from app import app
from users.model import User
from flask import Flask,request


@app.route('/users/signup', methods=['GET'])
def signup():
    return User().signup()


