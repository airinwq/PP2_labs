import csv
from db import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_user(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name, phone = row
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def update_user(old_name, new_name=None, new_phone=None):
    conn = get_connection()
    cur = conn.cursor()
    if new_name:
        cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE name = %s", (new_phone, old_name))
    conn.commit()
    cur.close()
    conn.close()

def search_users(filter_by_name=None, filter_by_phone=None):
    conn = get_connection()
    cur = conn.cursor()
    if filter_by_name:
        cur.execute("SELECT * FROM PhoneBook WHERE name ILIKE %s", ('%' + filter_by_name + '%',))
    elif filter_by_phone:
        cur.execute("SELECT * FROM PhoneBook WHERE phone ILIKE %s", ('%' + filter_by_phone + '%',))
    else:
        cur.execute("SELECT * FROM PhoneBook")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

def delete_user(name_or_phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM PhoneBook WHERE name = %s OR phone = %s", (name_or_phone, name_or_phone))
    conn.commit()
    cur.close()
    conn.close()

# Пример меню
if __name__ == "__main__":
    create_table()
    while True:
        print("\n1. Добавить вручную")
        print("2. Загрузить из CSV")
        print("3. Обновить запись")
        print("4. Найти")
        print("5. Удалить")
        print("0. Выйти")
        choice = input("Выбор: ")

        if choice == "1":
            name = input("Имя: ")
            phone = input("Телефон: ")
            insert_user(name, phone)
        elif choice == "2":
            filename = input("Имя CSV файла: ")
            insert_from_csv(filename)
        elif choice == "3":
            old_name = input("Текущее имя: ")
            new_name = input("Новое имя (оставь пустым если не менять): ")
            new_phone = input("Новый телефон (оставь пустым если не менять): ")
            update_user(old_name, new_name or None, new_phone or None)
        elif choice == "4":
            f_name = input("Поиск по имени (Enter чтобы пропустить): ")
            f_phone = input("Поиск по телефону (Enter чтобы пропустить): ")
            search_users(f_name or None, f_phone or None)
        elif choice == "5":
            value = input("Имя или телефон для удаления: ")
            delete_user(value)
        elif choice == "0":
            break
        else:
            print("Неверный выбор")
