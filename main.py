import requests
from config import API_URL, API_KEY

user = {
    'cash': 1000000.0,
    'holdings': {
        'bitcoin': 0
    }
}

def cryptocurrencyPrice():
    headers = {'x-cg-demo-api-key': API_KEY}
    params = {'ids': 'bitcoin' , 'vs_currencies' : 'usd'}
    try:
        response = requests.get(API_URL, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data['bitcoin']['usd']
        else:
            print(f" API Error: Status {response.status_code}")
            return None
    except Exception as e:
        print(f" Error fetching price: {e}")
        return None

def show_wallet():
    print(f"Cash: {user['cash']:.2f} USD" )
    print(f"Holdings: {user['holdings']['bitcoin']:.2f} BTC" )

def show_cryptocurrencyPrice(data):
    print(data)

def get_crypto_ammount():
    while True:
        try:
            how_many = float(input("How many cryptocurrencies would you like to:  "))
            if how_many > 0.0:
                return how_many
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a number.")

def buy_crypto(how_many):
    price = cryptocurrencyPrice()
    if price is None:
        print("Failed to get price!")
        return

    totalPrice = price * how_many

    if user['cash'] >= totalPrice:
        user['cash'] -= totalPrice
        user['holdings']['bitcoin'] += how_many
    else:
        print("You don't have enough money!")


def sell_crypto(how_many):
    price = cryptocurrencyPrice()
    if price is None:
        print("Failed to get price!")
        return

    if user['holdings']['bitcoin'] >= how_many:
        valueSell = how_many * price
        user['holdings']['bitcoin'] -= how_many
        user['cash'] += valueSell
        print(f"Successfully sold {how_many} bitcoin for {valueSell}.")
    else:
        print("You don't have enough bitcoin to sell!")

def procced_exchange():
    print("\n --Choose an operation to proceed--")
    print("1. Buy cryptocurrency")
    print("2. Sell cryptocurrency")
    choice = input(": ")

    match choice:
        case "1":
            ammount_to_buy = get_crypto_ammount()
            if ammount_to_buy:
                buy_crypto(ammount_to_buy)

        case "2":
            ammount_to_buy = get_crypto_ammount()
            if ammount_to_buy:
                sell_crypto(ammount_to_buy)

def show_menu():
    print("Welcome in your crypto currency walllet")
    print("What Actions would you like to take")
    print("1. Check cypto/usd ammount")
    print("2. Check current cryptocurrency price")
    print("3. Buy/Sale some crypto")
    print("4. Exit")

#def get_crypto_symbols():



def ask_to_continue():
    choice = input("\n Do you want go back to menu? (Y/N): ")
    return choice.lower() == "y"

while True:
    show_menu()
    choice = int(input("Select an option: "))


    match choice:
            case 1:
                print("\n --Current Wallet Status--")
                show_wallet()
                if not ask_to_continue():
                    break

            case 2:
               print("\n --Current Bitcoin Price -- ")
               cryptoCurrencyPrice = cryptocurrencyPrice()
               if cryptoCurrencyPrice:
                 show_cryptocurrencyPrice(cryptoCurrencyPrice)
               if not ask_to_continue():
                   break

            case 3:
                procced_exchange()
                print("\n --Your wallet status after this operation--")
                show_wallet()
                if not ask_to_continue():
                    break
            case 4:
                break

