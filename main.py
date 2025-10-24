import requests

apiUrl = 'https://api.coingecko.com/api/v3/simple/price'
headers = { 'x-cg-demo-api-key': 'CG-YDaE1peLA15xdK6ZyEkwAbXz' }

UserParams = {
    'portfel': {
        'money': 1000000,
        'cryptocurrency': 0
    }
}

def menu():
    print("Welcome in your crypto currency walllet")
    print("What Actions would you like to take")
    print("1. Check cypto/usd ammount")
    print("2. Check crypto current exchange rate")
    print("3. Buy/Sale some crypto")
    print("4. Exit")

def cryptocurrencyPrice():
    response = requests.get(apiUrl, params={'ids': 'bitcoin', "vs_currencies": "usd"}, headers=headers)
    if response.status_code == 200:
        data = response.json()
        Bitcoin_price = data['bitcoin']['usd']
        print("Obecna cena bitcoina wynosi: " + str(Bitcoin_price))
        return Bitcoin_price
    else:
        print("Fail to get data")
        return None

def exchange():
    Bitcoin_price = cryptocurrencyPrice()
    money = UserParams['portfel']['money']

    if money >= Bitcoin_price:
        UserParams['portfel']['money'] -= Bitcoin_price
        UserParams['portfel']['cryptocurrency'] += 1
    else:
        print("You don't have enough money")


def ask_to_continue():
    wybor = input("\nChcesz wrócić do menu? (Y/N): ")
    return wybor.lower() == "y"

while True:
    menu()
    wybor = int(input("Select an option: "))

    match wybor:
            case 1:
                print("\n📊 Your wallet:")
                print("Money:", UserParams['portfel']['money'], "USD")
                print("Crypto:", UserParams['portfel']['cryptocurrency'], "BTC")

                if not ask_to_continue():
                    break

            case 2:
               cryptocurrencyPrice()
               if not ask_to_continue():
                   break

            case 3:
                exchange()
                if not ask_to_continue():
                    break

            case 4:
                break

