'''Создайте программу которая спрашивает у пользователя число N для 
генерации пароля а затем генерирует ему пароль длиною N символов.'''


import random

n = int(input("Что бы сгенерировать пароль,ведите число: "))
pas = ''
for x in range(n):
	pas += random.choice(list("1234567890dhwgcdyckusukjoaijdiauSIDCUJSICJSJC"))
print(pas)	