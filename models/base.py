from peewee import Model, SqliteDatabase

def table_name_gen(model_cls):
    name = model_cls.__name__
    return name.lower() + "s"

#Userdata - Locally persistance user settings, transaction history, balance, etc...
UserDB = SqliteDatabase("data/userdata.db",pragmas={'journal_mode': 'wal'})
class UserData(Model):
    class Meta:
        database = UserDB
        table_function = table_name_gen

#Masterdata - Local cache of price data, ship matrix, etc...
MasterDB = SqliteDatabase("data/masterdata.db",pragmas={"journal_mode":"wal"})
class MasterData(Model):
    class Meta:
        database = MasterDB
        table_function = table_name_gen

def close():
    if not UserDB.is_closed():
        UserDB.close()
    if not MasterDB.is_closed():
        MasterDB.close()
    