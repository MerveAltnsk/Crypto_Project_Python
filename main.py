import requests

# https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json

def get_crypto_data():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200:
        return response.json()

crpto_response = get_crypto_data()
user_input = input("Please enter a crypto currency: ")

for item in crpto_response:
    if item["currency"] == user_input:
        print(item["price"])
        break