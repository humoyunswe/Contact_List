import psycopg2

DB = 'postgres'  # Здесь надо написать вашу имя базы данных.
USER = 'postgres'  # Здесь надо написать ваше имя пользователя.
HOST = 'localhost'  # Здесь надо написать ваш хост.
PORT = 5432  # Если у вас другой порт, нужно изменить.
PASSWORD = 'humoyun'  # И пароль нужно ввести ваш.

connection = psycopg2.connect(database=DB, user=USER, password=PASSWORD, host=HOST, port=PORT)
cur = connection.cursor()

def table_of_contacts():
    cur.execute("CREATE TABLE IF NOT EXISTS contacts (id SERIAL PRIMARY KEY, name VARCHAR(120), number VARCHAR(15));")
    connection.commit()

def add(id:int, name:str, contact:str):
    cur.execute("INSERT INTO contacts (id, name, number) VALUES (%s, %s, %s)", (id, name, contact))
    connection.commit()
    print("Контакт успешно создан!")

def list_of_contacts():
    cur.execute("SELECT * FROM contacts;")
    members = cur.fetchall()
    if not members:
        print("Нет контактов пока!")
    else:
        print("Контакты: ")
        for member in members:
            print(f"    ID: {member[0]},\n    Name: {member[1]},\n    Phone number: {member[2]}")
            print()

def delete(name):
    cur.execute("DELETE FROM contacts WHERE name = %s", (name,))
    connection.commit()
    print("Контакт успешно удален!")

def main():
    table_of_contacts()

    while True:
        print('''
    1. Добавить контакт
    2. Список контактов
    3. Удалить контакт
    4. Выйти
    ''')
        request = int(input("Введите номер задачи: "))
        if request == 1:
            id = int(input("ID контакта: "))
            name = input("Имя контакта: ")
            phone_number = input("Номер контакта: ")
            add(id, name, phone_number)
        elif request == 2:
            list_of_contacts()
        elif request == 3:
            name = input("Имя контакта: ")
            delete(name)
        elif request == 4:
            print("Вы вышли из программы.")
            break
        else:
            print("Неправильная команда!")

if __name__ == '__main__':
    main()
