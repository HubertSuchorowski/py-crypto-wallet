import requests
class API:
    def __init__(self, API_URL, API_KEY):
        self.API_URL = API_URL
        self.API_KEY = API_KEY

    def cryptocurrency_price(self):
        headers = {'x-cg-demo-api-key': self.API_KEY}
        params = {'ids': 'bitcoin', 'vs_currencies': 'usd'}
        try:
            response = requests.get(self.API_URL, params=params, headers=headers)

            if response.status_code == 200:
                data = response.json()
                return data['bitcoin']['usd']
            else:
                print(f" API Error: Status {response.status_code}")
                return None
        except Exception as e:
            print(f" Error fetching price: {e}")
            return None
