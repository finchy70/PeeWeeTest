from database import *


for f in range(1, 20):
    new_entry = PeeData(col1=f, col2=f, col3=f, col4=f, col5=f)
    new_entry.save()

list =[]
for pee in PeeData.select():

    list.append(pee.col6)

print list


new_list = []
for things in PeeData.select().where(PeeData.col1 == 1):
    new_list += [(things.col1, things.col2, things.col3, things.col4, things.col5, things.col6)]

print new_list
print new_list[5][5]


