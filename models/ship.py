from models.base import MasterData, MasterDB
from peewee import CharField, FloatField, CompositeKey

class Ship(MasterData):
    manufacturer = CharField(max_length=200)
    model = CharField(max_length=200)
    variant = CharField(max_length=200,null=True)
    buy = FloatField(null=True)
    description = CharField(max_length=2500,null=True)

    class Meta:
        primary_key = CompositeKey("manufacturer","model","variant")
    
MasterDB.create_tables([Ship])