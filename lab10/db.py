import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="mydb",
        user="postgres",         
        password="airi_sm1",  
        host="localhost",
        port="5432"
    )
