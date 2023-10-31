# import json 

# def save_notes(notes, file_path): 
#     with open(file_path, 'w') as file: 
#         json.dump(notes, file, indent=4)

# def load_notes(file_path): 
#     with open(file_path, 'r') as file: 
#         notes = json.load(file) 
#         return notes
    

# def add_note(notes, new_note):
#     max_id = max(note['id'] for note in notes) if notes else 0 
#     new_note['id'] = max_id + 1 
#     notes.append(new_note)

# def edit_note(notes, note_id, new_title=None, new_body=None, new_datetime=None): 
#     for note in notes: 
#         if note['id'] == note_id: 
#             if new_title: 
#                 note['title'] = new_title 
#             if new_body: 
#                 note['body'] = new_body 
#             if new_datetime: 
#                 note['datetime'] = new_datetime 
#             break

# Задание: 
# Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок. 
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки. 
# Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). 
# Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), 
# можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.

import json
import datetime

# Функция для чтения заметок из файла
def read_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

# Функция для добавления заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена!")

# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новый текст заметки: ")
            note['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована!")
            return
    print("Заметка с указанным ID не найдена.")

# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена!")
            return
    print("Заметка с указанным ID не найдена.")

# Функция для вывода списка заметок
def list_notes():
    if len(notes) == 0:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"ID: {note['id']}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата/время создания/изменения: {note['timestamp']}")
            print()

# Функция для фильтрации заметок по дате
def filter_notes():
    date_str = input("Введите дату для фильтрации (гггг-мм-дд): ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        filtered_notes = [note for note in notes if datetime.datetime.strptime(note['timestamp'], "%Y-%m-%d %H:%M:%S").date() == date]
        if len(filtered_notes) == 0:
            print("Заметок с указанной датой нет.")
        else:
            for note in filtered_notes:
                print(f"ID: {note['id']}")
                print(f"Заголовок: {note['title']}")
                print(f"Текст: {note['body']}")
                print(f"Дата/время создания/изменения: {note['timestamp']}")
                print()
    except ValueError:
        print("Неверный формат даты.")

# Функция для обработки команд пользователя
def process_command(command):
    if command == 'add':
        add_note()
    elif command == 'edit':
        edit_note()
    elif command == 'delete':
        delete_note()
    elif command == 'list':
        list_notes()
    elif command == 'filter':
        filter_notes()
    elif command == 'exit':
        exit()
    else:
        print("Неверная команда.")

# Основной цикл программы
notes = read_notes()
while True:
    command = input("Введите команду (add, edit, delete, list, filter, exit): ")
    process_command(command)