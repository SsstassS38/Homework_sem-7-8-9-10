import model
import view


def start():
    choice = ''
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.information('\n Файл успешно открыт\n')
            case 2:
                model.save_file()
                view.information('\n Файл успешно сохранен\n')
            case 3:
                view.show_contacts(model.get_phone_book())
            case 4:
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
                view.information(f'\n Контакт {new_contact[0]} спешно создан\n')
            case 5:
                del_name = view.select_contact('Введите удаляемый контакт: ')
                contact = model.get_contact(del_name)
                if contact:
                    confirm = view.delete_confirm(contact[0][0])
                    if confirm:
                        model.delete_contact(contact[0])
                        view.information(f'\n Контакт {contact[0][0]} успешно удален\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request()
            case 6:
                name = view.select_contact('Введите контакт для изменения: ')
                contact = model.get_contact(name)
                if contact:
                    changed_contact = view.change_contact()
                    model.change_contact(contact[1], list(changed_contact))
                    view.information(f'n Контакт {contact[0][0]} спешно изменен\n')
                elif contact == []:
                    view.empty_request()
                else:
                    view.many_request() 
            case 7:
                find = view.find_contact()
                result = model.search_contact(find)
                view.show_contacts(result)
            case 8:
                view.end_program()
                break 