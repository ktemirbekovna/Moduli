import random
a = ('камень', 'ножницы', 'бумага')
s = input("напишите камень или ножницы или бумага: ")
b = random.choice(a)
if s == b:
    print("ничья")
elif (s == "камень") and (b == "бумага"):
    print("вы проиграли")
elif(s == "ножницы") and (b == "камень"):
    print("вы проиграли")
elif(s == "бумага") and (b == "ножницы"):
    print("вы проиграли")
else:
    print("вы выиграли")
print(s)
print(b)