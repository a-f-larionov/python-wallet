import decimal

from db import *


def db_add_user(name):
    print("add user" + name)
    w1 = Wallet(userName=name, sum=0)
    w1.save()


def db_user_add_money(name, income):
    print(" user income" + name + " " + income)
    w = Wallet.select().where(Wallet.userName == name).get()
    w.sum = w.sum + decimal.Decimal(income)
    w.save()


def db_show_list():
    html = ""
    query = Wallet.select()
    for row in query:
        html += row.userName + " " + str(row.sum) + " <br>"
    return html
