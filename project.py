import requests
import json

api_keys = "***"
api_url = f"https://v6.exchangerate-api.com/v6/{api_keys}/latest/"

source_currency = input("Source currency: ")  # USD
target_currency = input("Target currency: ")  # TRY

amount = int(input(f"How much {source_currency} do you want to exchange? "))
response = requests.get(api_url + source_currency)
response_json = json.loads(response.text)

print(response_json["conversion_rates"][target_currency])

print("1 {0} = {1} {2}.".format(source_currency,
                                 response_json["conversion_rates"][target_currency], target_currency))

print("{0} {1} = {2} {3}".format(amount, source_currency, amount *
                                  response_json["conversion_rates"][target_currency], target_currency))
