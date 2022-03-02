from peewee import *

walletDB = SqliteDatabase('wallet.db')


class Wallet(Model):
    sum = DecimalField()
    userName = CharField()

    class Meta:
        database = walletDB  # database here
