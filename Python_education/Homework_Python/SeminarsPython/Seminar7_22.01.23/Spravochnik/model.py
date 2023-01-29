# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Создать контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контакт
# 8. Выход из программы

phonebook = []

def init(value):           #инициализация функций меню
    if value == 1:
        open_file()
    elif value == 2:
        save_file()
    elif value == 3:
        show_contacts()
    elif value == 4:
        create_contacts()
    elif value == 5:
        delete_contacts()
    elif value == 6:
        change_contacts()
    elif value == 7:
        find_contacts()
    elif value == 8:
        exit()
    else:
        print("Некорректный выбор пункта меню")


# фукция открытия файла для дальнейшего использования
def open_file():
    path = 'Python\Python_education\Homework_Python\SeminarsPython\Seminar7_22.01.23\Spravochnik\data.txt'
    with open (path, "r") as data:
        file = data.read().split('\n') 
    print('Файл открыт')
    return file

# def show_contacts(): прописать ниже все функции меню

