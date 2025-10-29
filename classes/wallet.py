class Wallet:
    def __init__(self, cash, bitcoin):
        self.cash = cash
        self.bitcoin = bitcoin

    def show_wallet(self):
        print(f"Cash: {self.cash:.2f} USD")
        print(f"Holdings: {self.bitcoin:.8f} BTC")