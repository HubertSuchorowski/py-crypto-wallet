from classes.api import API
#from user import User
from classes.wallet import Wallet
from classes.exchange import Exchange
from classes.menu import Menu


def main():
    api = API('https://api.coingecko.com/api/v3/simple/price', "CG-YDaE1peLA15xdK6ZyEkwAbXz")
    wallet = Wallet()
    exchange = Exchange(wallet = wallet, api = api)
    menu = Menu(exchange = exchange)

    while True:
        choice = menu.show_main_menu()
        match choice:
                case 1:
                    print("\n --Current Wallet Status--")
                    wallet.show_wallet()
                    if not menu.ask_to_continue():
                        break

                case 2:
                   print("\n --Current Bitcoin Price -- ")
                   cryptocurrency_price = api.cryptocurrency_price()
                   if cryptocurrency_price:
                     print(f"1 BTC = {cryptocurrency_price}")
                   if not menu.ask_to_continue():
                       break

                case 3:
                    menu.proceed_exchange()
                    print("\n --Your wallet status after this operation--")
                    wallet.show_wallet()
                    if not menu.ask_to_continue():
                        break
                case 4:
                    break

if __name__ == "__main__":
    main()
