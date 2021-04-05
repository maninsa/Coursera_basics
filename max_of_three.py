#!/bin/python3.9
# Даны три целых числа
# Найдите наибольшее из них
# программа должна вывести ровно одно целое число

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))
if n1 > n2 > n3:
    print(n1)
elif n1 > n2 < n3:
