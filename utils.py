from sys import argv
from requests import get, utils
from decimal import Decimal  # Встроенный модуль decimal для работы с числами
from datetime import datetime

response = utils.get_unicode_from_response(get(('http://www.cbr.ru/scripts/XML_daily.asp')))

def currency_rates(code):
    content = response.split("<Valute ID=")  # получаем список
    for i in content:
        if code.upper() in i:
            print(datetime.strptime(content[0].split('"')[-4], '%d.%m.%Y').date(), ": ", code.upper(), sep="", end=" ")
            return Decimal(i.replace("/", "").split("<Value>")[1].replace(",", "."))

if __name__ == "__main__":
    word = argv[1]
    print(currency_rates(word))
