'''Спросите у пользователя 2 значения через input() а затем через модуль sys 
проверьте какое из 2-х значений занимает больше памяти.'''

import sys
a = input("Введите данные: ")
b = input("Введите данные: ")
print(sys.getsizeof(a))
print(sys.getsizeof(b))
