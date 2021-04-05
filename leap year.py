#!/bin/python3.9
# Дано натуральное число
# Требуется определить, является ли год с данным номером високосным
# Если год является високосным, то выведите YES, иначе выведите NO

year = int(input('Is this year are leap year?: '))
if year > 0 and year % 4 == 0:
    print('YES')
else:
    print("NO")