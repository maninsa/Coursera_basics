#!/bin/python3.9
# Даны два целых числa
# Программа должна вывести число "1", если первое число больше второго,
# число "2", если второе больше первого,
# число "0", если они равны.
# Эту задачу желательно решить с использованием каскадных инструкций if... elif... else.

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
if n1 > n2:
    print('1')
elif n1 < n2:
    print('2')
elif n1 == n2:
    print('0')
else:
    print('The fuck "ELSE"???')
