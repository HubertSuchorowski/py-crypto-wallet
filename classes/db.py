import sqlite3

connection = sqlite3.connect('database/crypto_app.db')
cursor = connection.cursor()

def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS wallet (
        cash FLOAT,
        bitcoin FLOAT
    )
    ''')
    connection.commit()

create_table()
