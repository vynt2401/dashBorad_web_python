import sqlite3


def get_connection():
    return sqlite3.connect('/run/media/ntv/MAIN/Python_testing/dash//day1/sql_dash.db')


def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Fruits (
        name TEXT NOT NULL,
        amount INTEGER,
        city TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

class addTable():
    def __init__(self, name, amount, city):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Fruits (name, amount, city) VALUES (?, ?, ?)", (name, amount, city))
        conn.commit()
        conn.close()
