'''Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", 
"Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"] 
и вытащите 4 рандомных имени оттуда и сохраните в другой список.'''

import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", 
"Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
names2 = []
c = 0
while c < 4:
    d = random.choice(names)
    c+=1
    names2.append(d)
    print(names2)


import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
names1 = []
a = random.choices(names, k = 4)
print(a)
names1.append(a)
print(names1)