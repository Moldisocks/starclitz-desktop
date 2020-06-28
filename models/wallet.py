import datetime

from peewee import FloatField, DateTimeField, IntegerField, ForeignKeyField

from models.base import UserData, UserDB
from models.trade import Trade


class Transaction(UserData):
    amount = FloatField()
    date_time = DateTimeField(default=datetime.datetime.now())
    trade = ForeignKeyField(Trade,null=True,unique=True)
    
    def __str__(self):
        return f"{self.date_time} {self.amount}"

def getTransactionHistory():
    return Transaction.select()
    

def getBalance():
    bal = float(0)
    res = getTransactionHistory()
    if not res:
        return 0
    for trans in res:
        bal += trans.amount
    return bal

def setBalance(balance:float):
    """Forcefully sets balance. Credits or debits to bring balance to passed amount
    """
    bal = getBalance()
    diff = balance - bal
    if diff != 0:
        t = Transaction()
        t.amount = float(diff)
        t.save()


UserDB.create_tables([Transaction])