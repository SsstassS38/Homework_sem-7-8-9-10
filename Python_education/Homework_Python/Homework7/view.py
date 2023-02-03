

commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']


def main_menu():
    print('Главное меню')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')
    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if 0 < choice < 9:
                return choice 
            else:
                print('Введите значение от 1 до 8')
        except ValueError:
            print('Введите корректное значение: ')

def show_contacts(phone_list: list):
    if len(phone_list) < 1: 
        print('телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:30} {contact[1]:20} {contact[2]:20}')
        print()

def input_error():
    print('Ошибка ввода, введите корректный пункт меню')

def end_program():
    print('До свидания! Программа завершена')

def empty_request():
    print('Искомый контакт не найден')

def many_request():
    print('Введите данные точнее, т.к. найдено более одного подходящего контакта')


def create_new_contact():
    name = input('Введите Имя и Фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def find_contact():
    find = input('Введите поисковой запрос: ')
    return find

def select_contact(message: str):
    contact = input(message)
    return contact

def delete_confirm(contact: str):
    result = input(f'Вы действительно хотите удалить контакт {contact}? (y/n): ').lower()
    if result == 'y':
        return True
    else:
        return False


def change_contact():
    print('Введите новые данные (если изменения не требуется, введите Enter) ')
    name = input('Введите Имя и Фамилию: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment


def information(message):
    print(message)
