# Поиск искомого символа в отдельном значении списка.
# my_list = ['sarew44tg', 'dsfjknkjnds54', 'sdfsdfc25', 'sadsdfc789']

# print(my_list)

# search = input('Введите искомое число: ')
# for item in my_list:
#     if search in item:
#         print(f'Искомое число {search} входит в заданный список')
#         break
# else:
#     print(f'Искомое число {search}  НЕ входит в заданный список')



# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"] #, ищем: "qwe", ответ: 3
#my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] #, ищем: "йцу", ответ: 5
#my_list = ["йцу", "фыв", "ячс", "цук", "йцукен"] @, ищем: "йцу", ответ: -1
#my_list = ["123", "234", 123, "567"] @, ищем: "123", ответ: 1
#my_list = [] @, ищем: "123", ответ: -1

# my_list = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# search = "йцу"
# position = 0
# print(my_list)
# count = 0
# for item in my_list:                                              #вариант Анастасии Булгаковой (не очень рабочий)
#         if search == item:
#             count+=1
#         if count == 2:
#             break
#         position +=1
# if count>=2:
#     print(position)



# print(my_list)
# flag = 0
# index = 0
# search = input('Введите искомую строку: ')
# for item in my_list:
#     if search == item:
#         flag += 1
#     if flag == 2:                                   #вариант Дмитрия Парсина (не работает чёта)
#         index == item
#         break
# if flag == 2:
#     print(f'Искомая строка символов {search} по второму вхождению находится под {index} позицией')
# else:
#     print(f'Искомой строки {search} нет в списке строк')



# list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"] #, ищем: "qwe", ответ: 3
# list_2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"] #, ищем: "йцу", ответ: 5
# list_3 = ["йцу", "фыв", "ячс", "цук", "йцукен"] #, ищем: "йцу", ответ: -1
# list_4 = ["123", "234", 123, "567"] #, ищем: "123", ответ: 1
# list_5 = [] #, ищем: "123", ответ: -1

# def proverka(my_list, search):
#     count = 0
#     index = 0
#     for i in my_list:
#         if i == search:
#             if count == 1:
#                 print(f'позиция второго вхождения {index}')             #Вариант Слободчикова гика (рабочий)
#                 break
#             count = 1
#         index += 1
#     else:
#         print('нет второго вхождения')

# proverka(list_1, 'qwe')
# proverka(list_2, 'йцу')
# proverka(list_3, 'йцу')
# proverka(list_4, '123')
# proverka(list_5, '123')
        
