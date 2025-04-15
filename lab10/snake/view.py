import psycopg2

conn = psycopg2.connect(
    dbname="mydb",  # или твое имя базы, если не "mydb"
    user="postgres",
    password="airi_sm1",  # заменяешь на свой
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT users.username, user_scores.score, user_scores.level, user_scores.saved_at FROM user_scores JOIN users ON users.id = user_scores.user_id ORDER BY saved_at DESC;")
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
