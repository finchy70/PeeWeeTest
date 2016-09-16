from database import *

toyota = Car(model="Toyota")
toyota.save()

add_data = Name.create(name="Paul", car=toyota)

add_data.save()

for cars in Name.select().where(Name.name=="Paul"):
    print cars.car