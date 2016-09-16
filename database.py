from peewee import *
from datetime import date


database = SqliteDatabase('database.sqlite', **{})


class BaseModel(Model):
    class Meta:
        database = database


class Car(BaseModel):
    model = CharField()

    class Meta:
        db_table = "car"


class Name(BaseModel):
    car = ForeignKeyField(Car, related_name="cars")
    name = CharField()


    class Meta:
        db_table = 'name'

database.connect()
database.create_tables([Car, Name], safe=True)

add_cars = Car(model="Toyota")
add_cars.save()