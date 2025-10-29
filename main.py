from api import API
#from user import User
from wallet import Wallet
from exchange import Exchange
from menu import Menu


def main():
    api = API('https://api.coingecko.com/api/v3/simple/price', "CG-YDaE1peLA15xdK6ZyEkwAbXz")
    wallet = Wallet(1000000, 0)
    exchange = Exchange(wallet = wallet, api = api)
    menu = Menu()

    def procced_exchange():
        choice = menu.show_exchange_menu()
        match choice:
            case "1":
                ammount_to_buy = exchange.get_crypto_ammount()
                if ammount_to_buy:
                    exchange.buy_crypto(ammount_to_buy)

            case "2":
                ammount_to_buy = exchange.get_crypto_ammount()
                if ammount_to_buy:
                    exchange.sell_crypto(ammount_to_buy)

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
                   cryptoCurrencyPrice = api.cryptocurrencyPrice()
                   if cryptoCurrencyPrice:
                     print(f"1 BTC = {cryptoCurrencyPrice}")
                   if not menu.ask_to_continue():
                       break

                case 3:
                    procced_exchange()
                    print("\n --Your wallet status after this operation--")
                    wallet.show_wallet()
                    if not menu.ask_to_continue():
                        break
                case 4:
                    break

if __name__ == "__main__":
    main()
