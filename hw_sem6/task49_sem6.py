# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной
# import os
# import time

fileName = 'telephone_book.txt'

def readFile(file_name):
    result = []
    with open(file_name, 'r+') as data:
        for line in data: 
            result.append(line.split())
    return result

def search_data():
    while True:
        answer = input("Строка поиска(Еnter - выход): ")
        if answer == "":
            return
        result = []
        with open('telephone_book.txt', "r", encoding="utf8") as datafile:
            for line in datafile:
                result.append(line.strip("\n"))
        result = list(filter(lambda line: answer in line, result))
        return result


def add_data():
    while True:
        print('Добавление записи (Еnter - выход): ')
        last_name = input("Фамилия: ")
        if last_name == "":
            return
        first_name = input("Имя: ")
        patronymic = input("Отчество: ")
        phone_number = input("Номер телефона: ")
        data_to_save = [last_name, first_name, patronymic, phone_number]
        if "" in data_to_save:
            return
        data_to_save = ", ".join(data_to_save) + "\n"
        print(f'Добавлена запись: {data_to_save}')
        with open('telephone_book.txt', "a", encoding="utf8") as datafile:
            datafile.writelines(data_to_save)

def search_in_file(request):
    result = []
    with open('telephone_book.txt', "r", encoding="utf8") as datafile:
        for line in datafile:
            result.append(line.strip("\n"))
        result = list(filter(lambda line: request in line, result))
    return result

def delete_data():
    while True:
        answer = input("Строка поиска для удаления (Enter - выход): ")
        if answer == "":
            return
        records = search_in_file(answer)
        if len(records) == 0:
            print("Нет записей для удаления")
        else:
            print("Такая запись есть. Удалить?")
            if input('Удалить [Y/N]').upper() == "Y":
                phonedata = ""
                with open('telephone_book.txt', "r", encoding="utf8") as datafile:
                    for line in datafile:
                        if answer in line:
                            continue
                        phonedata += line
                with open('telephone_book.txt', "w", encoding="utf8") as datafile:
                    datafile.write(phonedata)
                    print("Запись удалена")


menu = [("Введите номер действия: \n"
    "1 - Показать все записи\n"
    "2 - Добавить новый контакт\n"
    "3 - Поиск\n"
    "4 - Удалить контакт\n"
    "5 - Выход")]
    
while True:

    for i in menu:
        print(i)

    text = input("Введите номер: ")
    if text == '1':
        print(readFile(fileName))
    elif text == '2':
        add_data()
    elif text == '3':
        print(search_data())
    elif text == '4':
        delete_data()
    elif text == '5':
        exit()

