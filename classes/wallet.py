import sqlite3

class Wallet:
    def __init__(self, db_connection = 'database/crypto_app.db'):
        self.db_connection = db_connection
        self.connection = sqlite3.connect(self.db_connection)
        self.cursor = self.connection.cursor()
        self.load_wallet_data()

    def load_wallet_data(self):
        self.cursor.execute('''SELECT cash, bitcoin FROM wallet''')
        data = self.cursor.fetchone()
        if data:
            self.cash, self.bitcoin = data
            return self.cash, self.bitcoin
        else:
            print("Adding default wallet")
            self.cash = 100000
            self.bitcoin = 0
            self.cursor.execute(
                "INSERT INTO wallet VALUES (?, ?)", (self.cash, self.cash)
            )
            self.connection.commit()
            return self.cash, self.bitcoin

    def save_wallet_data(self):
        self.cursor.execute("UPDATE wallet SET cash = ?, bitcoin = ?", (self.cash, self.bitcoin))
        self.connection.commit()

    def show_wallet(self):
        print(f"Cash: {self.cash:.2f} USD")
        print(f"Holdings: {self.bitcoin:.8f} BTC")