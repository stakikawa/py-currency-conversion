import requests
from decimal import Decimal


class RatesNotAvailableError(Exception):
    pass

class CurrencyRate:

    def _source_url(self):
        return "https://api.exchangeratesapi.io/latest"

    def _decode_rates(self, response):
        rates = response.json().get('rates')
        for k, v in rates.items():
            rates[k] = Decimal(v)
        return rates

    def _decode_rate(self, response):
        [(k, v)] = response.json().get('rates').items()
        return Decimal(v)

    def get_rate_all(self, base):
        params = {'base': base}
        response = requests.get(self._source_url(), params)
        if response.status_code == 200:
            rates = self._decode_rates(response)
            return rates
        raise RatesNotAvailableError("Currency Rate Source Not Available")

    def get_rate(self, base, target):
        params = {'base': base, 'symbols': target}
        response = requests.get(self._source_url(), params)
        if response.status_code == 200:
            rate = self._decode_rate(response)
            return rate
        raise RatesNotAvailableError("Currency Rate Source Not Available")

    def convert(self, base, target, amount):
        rate = self.get_rate(base, target)
        return round(Decimal(amount * rate), 2)
