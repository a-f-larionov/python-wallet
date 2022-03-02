from models import *

walletDB.connect()

walletDB.create_tables([Wallet])
