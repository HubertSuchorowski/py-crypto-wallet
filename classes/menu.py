class Menu():
    def __init__(self, exchange):
        self.exchange = exchange

    def show_main_menu(self):
        print("Welcome in your crypto currency walllet")
        print("What Actions would you like to take")
        print("1. Check cypto/usd amount")
        print("2. Check current cryptocurrency price")
        print("3. Buy/Sale some crypto")
        print("4. Exit")

        while True:
            try:
                choice = int(input("Select an opertion(1-4)"))
                if  1 <= choice <= 4:
                    return choice
                else:
                    print("Invalid choice")
            except ValueError:
                print("Invalid choice")


    def show_exchange_menu(self):
        print("\n --Choose an operation to proceed--")
        print("1. Buy cryptocurrency")
        print("2. Sell cryptocurrency")

        while True:
            choice = input("Select an operation(1,2): ")
            if choice in ["1","2"]:
                return choice
            else:
                print("Invalid choice")

    def proceed_exchange(self):
        choice = self.show_exchange_menu()
        match choice:
            case "1":
                amount_to_buy = self.exchange.get_crypto_amount()
                if amount_to_buy:
                    self.exchange.buy_crypto(amount_to_buy)

            case "2":
                amount_to_buy = self.exchange.get_crypto_amount()
                if amount_to_buy:
                    self.exchange.sell_crypto(amount_to_buy)



    def ask_to_continue(self):
        choice = input("\n Do you want go back to menu? (Y/N): ")
        return choice.lower() == "y"

