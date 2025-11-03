import sqlite3
from email.policy import default

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

def load_wallet_data():
    cursor.execute('''SELECT cash, bitcoin FROM wallet''')
    data = cursor.fetchone()
    if data:
        cash, bitcoin = data
        return cash, bitcoin
    else:
        print("Adding default wallet")
        default_cash = 100000
        default_bitcoin = 0
        cursor.execute(
            "INSERT INTO wallet VALUES (?, ?)", (default_cash, default_bitcoin)
        )
        connection.commit()
        return default_cash, default_bitcoin

def save_wallet_data(cash, bitcoin):
    cursor.execute("UPDATE wallet SET cash = ?, bitcoin = ?",(cash, bitcoin))
    connection.commit()

create_table()
