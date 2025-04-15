import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="mydb",
        user="postgres",
        password="airi_sm1",  # ← сюда впиши свой пароль
        host="localhost",
        port="5432"
    )

# Проверка, есть ли пользователь
def get_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result

# Добавление нового пользователя
def create_user(username):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return user_id

# Сохранение очков
def save_score(user_id, score, level):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO user_scores (user_id, score, level) VALUES (%s, %s, %s)", 
                (user_id, score, level))
    conn.commit()
    cur.close()
    conn.close()
