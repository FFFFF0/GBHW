import requests
from decimal import *


def currency_rates(num):
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text
    if (num) not in response:
        print(None)
    rur = response[response.find('<Value>', response.find(num)) + 7:response.find('</Value>', response.find(num))]
    return f"{Decimal(rur.replace(',', '.'))}"


print(currency_rates("Дол"))
print(currency_rates("Евр"))
