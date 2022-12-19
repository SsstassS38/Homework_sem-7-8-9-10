# Файлы
# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()


# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


# Функции
# Это фрагмент программы, используемый
# многократно

# import Hello as h
# print(h.f(1))          #выдернуть данные из другого файла в папке (файл Hello добавить в папку с 1 лекции и добавить. сейчас его нет)


# def new_string(symbol, count = 3):
#     return symbol * count

# print(new_string('!', 5))    
# print(new_string('!', 3))
# print(new_string(4))     


# def concatenatio(*params):
#     res: str = ""             # res: int = 0             # СКЛЕИВАНИЕ СИМВОЛОВ, ЧИСЕЛ В СТРОКУ СТРОК ИЛИ ЧИСЕЛ
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))   # asdw
# print(concatenatio('a', '1')  )           # a1)
# print(concatenatio(1, 2, 3, 4))           # 10  

# def fib(n):                                              # РЕКУРСИЯ
#     if n in [1, 2]:
#         return 1                      
#     else:   
#         return fib(n - 1) + fib(n - 2)

# list = []
# for e in range(1, 20):
#     list.append(fib(e))
# print(list)                                             # нахождение чисел фибоначи
    


# a = (3, 4, 41, 5)                                       # КОРТЕЖИ.  (tuple)
# print(a)                                                # если аргументы в скобках c запятой - это уже кортеж! 
# print(a[-2])

# Кортеж - это неизменяемый список
# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')


# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support item assignment           # не изменияемый список как пример ошибки

# Распаковка кортежа на отдельные переменные

# t = tuple(['red', 'green', 'blue'])                                                    #Двойное преобразование [списка] в (кортеж)
# red, green, blue = t                                                                   # Распаковка кортежа в переменные
# print('r:{} g:{} b:{}'.format(red, green, blue))
# # r:red g:green b:blue


 
                                                                           #СЛОВАРИ

# dictionary = {}
# dictionary = \
#     {
#     'up': '↑',                 #ключ 'up'         "\" вставлять для того, чтобы не писать в одну строку словарь 
#     'left': '←',
#     'down': '↓',
#     'right': '→'
#     }
# # print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left']) # ←                #печать отдельного значения по ключю
# # типы ключей могут отличаться

# # for k in dictionary.values():
# #     print(k)                                 # печать значений словаря через проход циклом. 1 вариант

# # for v in dictionary:
# #     print(v)                                 # печать элементов спсика (ключей) словаря через проход циклом

# # for v in dictionary:
# #     print(dictionary[v])                       # печать значение спсика словаря через проход циклом


# print(dictionary['up'])        # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# # print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#  print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# down: ↓
# right: →


                                                                    # МНОЖЕСТВА
                                                       # Неупорядоченная совокупность элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1,} 


# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}           # удаление значения если оно есть, то ок, если нет, то...
# # colors.remove('red')                                # KeyError: 'red'
# colors.discard('red') # ok                         # удаление значения без ошибок
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()



# a = {1, 2, 3, 5, 8}
# print(a)
# b = {2, 5, 8, 13, 21}
# print(b)
# c = a.copy() # c = {1, 2, 3, 5, 8}
# print(c)
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# print(u)
# i = a.intersection(b) # i = {8, 2, 5}
# print(u)
# dl = a.difference(b) # dl = {1, 3}
# print(dl)
# dr = b.difference(a) # dr = {13, 21}
# print(dr)
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q)
# # {1, 21, 3, 13}


                                                                    #Неизменяемое множество
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})

                                                                    # ЛИСТЫ
list1 = [1, 2, 3, 4, 333]
list2 = list1
for e in list1:
    print(e)

print()

for e in list2:
    print(e)

                                                                    