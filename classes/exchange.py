class Exchange:
    def __init__(self, wallet, api):
        self.wallet = wallet
        self.api = api

    @staticmethod
    def get_crypto_amount():
        while True:
            try:
                how_many = float(input("How many cryptocurrencies would you like to:  "))
                if how_many > 0.0:
                    return how_many
                else:
                    print("Please enter a number greater than 0.")
            except ValueError:
                print("Please enter a number.")


    def buy_crypto(self, how_many):
        price = self.api.cryptocurrency_price()
        if price is None:
            print("Failed to get price!")
            return

        totalPrice = price * how_many

        if self.wallet.cash >= totalPrice:
            self.wallet.cash -= totalPrice
            self.wallet.bitcoin += how_many
        else:
            print("You don't have enough money!")

    def sell_crypto(self, how_many):
        price = self.api.cryptocurrencyPrice()
        if price is None:
            print("Failed to get price!")
            return

        if self.wallet.bitcoin >= how_many:
            valueSell = how_many * price
            self.wallet.bitcoin -= how_many
            self.wallet.cash += valueSell
            print(f"Successfully sold {how_many} bitcoin for {valueSell}.")
        else:
            print("You don't have enough bitcoin to sell!")


