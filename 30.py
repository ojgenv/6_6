"""Задача 30:  Заполните массив элементами арифметической прогрессии.
 Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
 Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

a1 = int(input('Введите первый элемент '))
d = int(input('Введите разность '))
max = int(input('Введите количество элементов '))
n = 1

myList = []

while (n <= max):
    myList.append(a1 + (n - 1) * d)
    n += 1

print (myList)