#!/usr/bin/python3
""" a script that starts a Flask web application with a given route """
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """a simple function to return text """
    return "Hello HBNB!"


@app.route("/hbnb")
def projectname():
    """a funtion that displays a given return value"""
    return "HBNB"


if __name__ == "__main__":
    app.run()
