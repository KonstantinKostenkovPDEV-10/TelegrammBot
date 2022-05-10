import requests
import json
from config import currency, headers

class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(quote, base, amount):
        try:
            quote_key = currency[quote.lower()]
        except KeyError:
            raise APIException(f"Валюта {quote} не найдена!")
        try:
            base_key = currency[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        if quote_key == base_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency[base.lower()]}&from={currency[quote.lower()]}&amount={amount}"
        payload = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        res = json.loads(response.content)
       1 total_price = round(res["result"], 2)
        message = f"Цена {amount} {quote} в {base} : {total_price}"
        return message
