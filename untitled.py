import random
names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
grupp1 = []
grupp2 = []
grupp3 = []
grupp4 = []
i=0
while i < 4:
 c = random.choice(names)
 i+=1
 grupp1.append(c)
 grupp2.append(c)
 grupp3.append(c)
 grupp4.append(c)
print( grupp1, grupp2, grupp3, grupp4 )