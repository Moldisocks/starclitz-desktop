from peewee import FloatField, DateTimeField, IntegerField, ForeignKeyField, UUIDField

from models.base import UserData, UserDB

class Trade(UserData):
    uuid = UUIDField

#Mini calc
class miniCalcTrade(UserData):
    buyPrice = FloatField()
    sellPrice = FloatField()
    cargo = IntegerField()
    balance = 0
    
    def getUnitCount(self):
        unitCount = round(self.balance / self.buyPrice)
        if unitCount > self.cargo:
            unitCount = self.cargo
        return unitCount
    def getCapital(self):
        return (self.getUnitCount() * self.buyPrice)
    def getReturn(self):
        return (self.getUnitCount() *self.sellPrice)
    def getProfit(self):
        return (self.getReturn() - self.getCapital())
    def getProfitCeiling(self):
        return ((self.getProfit() / self.getUnitCount()) * self.cargo)


# class commodity(model):
#     def __init__(self):
#         self.fields = {"name":str(),"price":float(),"category":str(),"legal":bool(),"volatile":bool()}
#         super().__init__("commodities","data/local_cache.db")

# class tradeport(model):
#     def __init__(self): 
#         self.fields = {"name":str(),"parent":int()}
#         super().__init__("tradeports","")

UserDB.create_tables([Trade,miniCalcTrade])
