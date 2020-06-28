from peewee import *
from models.base import MasterData, MasterDB

class Commodity(MasterData):
    name = CharField(max_length=200)
    description = CharField(max_length=2500, null=True)
    buy = FloatField(null=True)
    sell = FloatField(null=True)

MasterDB.create_tables([Commodity])