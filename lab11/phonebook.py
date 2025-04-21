import psycopg2


conn = psycopg2.connect(database="mydb", user="postgres", password="airi_sm1", host="localhost", port=5432)
cursor = conn.cursor()


def insert_update_user(f_name, s_name, number):
    command = "CALL insert_update_user(%s, %s, %s);"
    cursor.execute(command, (f_name, s_name, number))
    conn.commit()
    print("Data inserted or updated successfully.")


def pattern_search(pattern):
    command = "SELECT * FROM pattern_search(%s);"
    cursor.execute(command, (pattern,))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No matching records found.")


def delete_user(info):
    command = "CALL delete_user(%s);"
    cursor.execute(command, (info,))
    conn.commit()
    print("User deleted successfully.")


def main():
    while True:
        print("\nChoose an option:")
        print("1. Insert or Update User")
        print("2. Search by Pattern")
        print("3. Delete User")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            f_name = input("Enter First Name: ")
            s_name = input("Enter Second Name: ")
            phone = input("Enter Phone Number: ")
            insert_update_user(f_name, s_name, phone)
        elif choice == '2':
            pattern = input("Enter pattern to search for: ")
            pattern_search(pattern)
        elif choice == '3':
            info = input("Enter name or phone number to delete: ")
            delete_user(info)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

# Запуск программы
main()

# Закрытие соединения
cursor.close()
conn.close()
