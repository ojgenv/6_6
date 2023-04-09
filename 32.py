"""Задача 32: Определить индексы элементов массива (списка),
 значения которых принадлежат заданному диапазону (т.е. не меньше заданного
   минимума и не больше заданного максимума)"""

import random

def getRandomList(a):
    myList = []
    for i in range(a):
        myList.append(random.randint(0,20))
    return(myList)

myList = getRandomList(20)
print(myList)

min = int(input('Введите минимальный '))
max = int(input('Введите максимальный '))
myNewList = []

for i in range(20):
    if myList[i] >= min and myList[i] <= max:
        myNewList.append(i)

print (myNewList)