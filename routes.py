from logic import *
from markupsafe import escape

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return \
        "<a href='/show_list'>list</a><br>" \
        "<a href='/add_user'>add_user</a><br>"


@app.route("/add_user/<name>")
def add_user(name):
    db_add_user(name)
    return f"Hello, {escape(name)}!"


@app.route("/income/<name>/<income>")
def user_add_money(name, income):
    db_user_add_money(name, income)
    return "OK"


@app.route("/show_list")
def show_list():
    return db_show_list()
