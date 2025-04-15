import psycopg2
from db import get_connection

# Функция для получения данных из таблицы phonebook
def view_phonebook():
    conn = get_connection()
    cur = conn.cursor()
    
    # Выполняем запрос, чтобы получить все данные из таблицы phonebook
    cur.execute("SELECT * FROM phonebook;")
    
    # Получаем все строки из таблицы
    rows = cur.fetchall()

    # Выводим все данные
    for row in rows:
        print(row)

    # Закрываем соединение
    cur.close()
    conn.close()

view_phonebook()  # Вызываем функцию, чтобы показать данные
