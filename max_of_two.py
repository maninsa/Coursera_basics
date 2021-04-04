#!/bin/python3.9

# Напишите программу, которая считывает два целых числа A и B
# и выводит наибольшее значение из них.
# Числа —  целые от 1 до 1000.

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
if n1 > n2:
    print(n1)
if not (n1 > n2):
    print(n2)
if n1 == n2:
    print('Worth it')
# Почему при равенстве чисел печатается цифра, а не только 'мой текст'?

