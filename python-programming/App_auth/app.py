from flask import Flask
from users import routes

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)
