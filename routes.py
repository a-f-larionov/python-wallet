from logic import *
from markupsafe import escape

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return \
        "<a href='/show_list'>list</a><br>" \
        "<a href='/add_user/user_name'>add_user</a><br>"\
        "<a href='/income/user_name/123'>income</a><br>"


@app.route("/add_user/<name>")
def route_add_user(name):
    db_add_user(name)
    return f"Hello, {escape(name)}!"


@app.route("/income/<name>/<income>")
def route_income(name, income):
    db_user_add_money(name, income)
    return "OK"


@app.route("/show_list")
def route_show_list():
    return db_show_list()
