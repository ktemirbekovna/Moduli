'''Напишите программу которая будет принимать аргументы sys.argv 
и выводить на экран оттуда всё что передал пользователь.'''


import sys
a = input("Введите данные: ")
sys.stderr.write(a)
sys.stderr.flush()
print(sys.argv) 

import sys
sys.stderr.write(input("Введите данные "))
sys.stderr.flush()
print(sys.argv) 