# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#Первый вариант решения
# from decimal import Decimal
# import random

# list = []
# values = 0
# for i in range(5):
#     values = round(random.uniform(0, 10), 2) 
#     list.append(values)
# min = list[0]
# max = 0
# for i in range(len(list)):
    
#     if max < list[i]:
#         max = list[i]
#     if min > list[i]:
#         min = list[i]
# dif = (max - int(max)) - (min - int(min))

# print(list)
# print(max, min)
# print(round(dif,2))

#второй вариант решения

from random import uniform

# n = int(input('Введите размер списка '))
# list1 = [round(uniform(0,9),2) for i in range(n)]

# min = min(list1, key=lambda i: float(i))
# max = max(list1, key=lambda i: float(i))

# dif = (max - int(max)) - (min - int(min))

# print(list1)
# print(max, min)
# print(round(dif,2))

# Третий вариант решения с оптимизацией кода

lst = list(map(float, input("Введите числа через пробел:\n").split()))
new_lst = [round(i%1,2) for i in lst if i%1 != 0]                                 
print(max(new_lst) - min(new_lst))