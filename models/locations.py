from peewee import *

from models.base import MasterDB, MasterData
from models.commodity import Commodity


class Location(MasterData):
    name = CharField(max_length=200)
    commodities = ManyToManyField(Commodity)
    station = CharField(max_length=200,null=True)
    moon = CharField(max_length=200,null=True)
    planet = CharField(max_length=200,null=True)
    system = CharField(max_length=200)
    description = CharField(max_length=2500,null=True)

    class Meta:
        primary_key = CompositeKey("name","system")
    
    def getHierarchy(self):
        buildStr = str()
        if self.system is not None:
            buildStr += f"/{self.system}/"
        if self.planet is not None:
            buildStr += f"{self.planet}/"
        if self.moon is not None:
            buildStr += f"{self.moon}/"
        if self.station is not None:
            buildStr += f"{self.station}/"
        if self.name is not None:
            buildStr += f"{self.name}/"
        return buildStr
    def __str__(self):
        return self.getHierarchy()

MasterDB.create_tables([Location])