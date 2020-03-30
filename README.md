# PyCurrencyConversion
PyCurrencyConversion is a free library for foreign exchange rates and conversions.

## Features:
- Show all conversion rates for one currency (ex. USD to all others)
- Show conversion rate for one currency to another (ex. CAD to CNY)
- Convert amount from one currency to another (ex. USD $10 to CNY)

## Source:
The conversion rates are taken from https://exchangeratesapi.io/, a free API published by the European Central Bank.

## Installation:
Directly clone repository, then

    python setup.py install
    
## Examples:
Initialize class:

    python
    >>> from py_currency.currency_rates import CurrencyRate
    >>> c = CurrencyRate()
    
Show all conversion rates for one currency:

    >>> c.get_rate_all('USD')
    {'CAD': Decimal('1.4161682073999999342817091019242070615291595458984375'), 'HKD': Decimal('7.75412361790000037586878534057177603244781494140625'), ...}

Show conversion rate for one currency to another:

    >>> c.get_rate('USD', 'JPY')
    Decimal('108.1566068515000011984739103354513645172119140625')

Convert amount from one currency to another:
    
    >>> c.convert('JPY', 'USD', 25000)
    Decimal('231.15')
    


