# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
 
# num = input('Введите дробное число: ')
# num = num.replace('.', '')
# my_list = list(num)
# my_listNum = map(int, my_list)
# res = sum(my_listNum)
# print(res)

# Решение с оптимизацией кода

def sum_digits(num):
    return sum(map(int, num.replace('.','')))
num = input('Введите любое вещественное число: ')
print(f'Сумма цифр в этом числе равна {sum_digits(num)}')