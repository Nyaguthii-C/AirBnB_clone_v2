#!/usr/bin/python3
"""
a script that starts a Flask web application with a given route
taking a variable with an integer value in the url path
"""
from flask import Flask
from markupsafe import escape
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


@app.route("/c/<text>")
def c_lang(text):
    """takes the variable text as part of url path"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


@app.route("/python")
def python_lang(text="is cool"):
    """function with a variable having default value as part of url path"""
    return 'Python ' + text.replace('_', ' ')


@app.route("/python/<text>")
def python_is(text):
    """takes the variable text as part of url path"""
    text = text.replace("_", " ")
    return f"Python {escape(text)}"


@app.route("/number/<int:n>")
def int_number(n):
    """returns a number only if it is an integer"""
    return f"{n} is a number"


if __name__ == "__main__":
    app.run()
