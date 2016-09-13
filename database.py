from peewee import *
from datetime import date


database = SqliteDatabase('peeweetest.db', **{})


class BaseModel(Model):
    class Meta:
        database = database


class PeeData(BaseModel):
    col1 = IntegerField(null=True)
    col2 = IntegerField(null=True)
    col3 = IntegerField(null=True)
    col4 = IntegerField(null=True)
    col5 = IntegerField(null=True)
    col6 = DateField(default=date.today())

    class Meta:
        db_table = 'testdata'

database.connect()
database.create_table(PeeData, safe=True)

