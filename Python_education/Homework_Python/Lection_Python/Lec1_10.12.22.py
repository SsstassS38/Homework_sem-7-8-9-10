# Переменные/ Типы данных справедливы
# int, float, boolean, str
# list и др.

#value = None 

# a = 123
# b = 1.23
# print(type(a))   #печать типа переменной
# print(type(b))
# value = 12345
# print(type(value))

# s = 'hello world'
# print(s)      #вывод строки
# print(a, b, s)
# print(a, '-', b, '-', s)
# print('{2} - {1} - {0}' .format(a, b, s))
# print(f'{a} - {b} - {s}')
# f = False
# print(f)

#list = [1, 2, 3, 4, 'hello']
#print(list)

#print('введите a'); 
#a = int(input())  # или float и т.д.
#print('введите b');
#b = int(input())
#print(a, ' + ', b, ' = ', a+b)
#print('{} {}'.format(a, b))
#print(f'{a} {b}')

#Ввод и вывод данных
#a = input('a = ')
#b = input('b = ')
#if a > b:
#    print(a)
#else:
#    print(b)

# Сокращённые операции и операции присваивания
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

#Управляющие конструкции: if, elif, else
#username = input('Введите ваше имя ')
#if username == 'Маша':
#    print('Ура, это же Маша')
#elif username == 'Марина':
#    print('Я так ждала Вас, Марина')
#elif username == 'Ильнар':
#    print('Ильнар - топ')
#else:
#    print('Привет, ', username)

#Управляющие конструкции: while-else
#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#else:
#    print('Пожалуй ')
#    print('хватит )')
#print(inverted)

#Управляющие конструкции: for
#for i in [1, 2, 3, 4, 5]:
#    print(i ** 2)

#list = [1, 2, 3, 10, 5]
#for i in [1, 2, 3, 4, 5]:
#    print(i)

# Знакомьтесь – range
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#  print(i)
# # 100 80 60 40 20
# for i in range(5):
#  print(i)
# # 0 1 2 3 4

#r = range(10)   
#for i in r:       # перебор чисел от 1 до 9
#    print(i)


#for i in range(2, 10, 3): #перебор чисел от 2 до 10 с шагом 3
#    print(i)    

#for i in 'qwerty':
#    print(i)


#Вложенные циклы
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#             line += "*"
#             print(line)

#Немного о строках:
# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #
# for c in text:
#     print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # print(text)
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# # Списки: введение
# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6))
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#    i *= 2
#    print(i) # [20, 4, 6, 8, 10]
# print(numbers)

# colors = ['red', 'green', 'blue']
# # for e in colors:
# #  print(e) # red green blue
# # for e in colors:
# #  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент
# print(colors)

# # Функции
# def f(x):
#     return x**2
# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# arg = 2
# print(f(arg))
# print(type(f(arg)))