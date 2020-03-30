from decimal import Decimal
from py_currency.currency_rates import (CurrencyRate, RatesNotAvailableError)
import pytest


class TestGetRateAll:

    def test_get_rates_valid_code(self):
        c = CurrencyRate()
        rates = c.get_rate_all('USD')

        # Test that rates is a dict
        assert (isinstance(rates, dict))

        # Test that rates has at least 1 key-value pair
        assert (len(rates) > 1)

        # Test that each rate is of type Decimal
        assert (isinstance(rates.get('CAD'), Decimal))

    def test_get_rates_invalid_code(self):
        c = CurrencyRate()

        # Test that error is raised when given invalid code
        with pytest.raises(RatesNotAvailableError):
            c.get_rate_all('ABC')


class TestGetRate:

    def test_get_rates_valid_code(self):
        c = CurrencyRate()
        base = 'CAD'
        target = 'CNY'
        rate = c.get_rate(base, target)

        # Test that rate is of type Decimal
        assert (isinstance(rate, Decimal))

    def test_get_rates_same_currency(self):
        c = CurrencyRate()
        base = 'CNY'
        target = 'CNY'
        rate = c.get_rate(base, target)

        # Test that rate of the same currency is 1
        assert (rate == Decimal(1))

    def test_get_rates_invalid_code(self):
        c = CurrencyRate()

        # Test that error is raised when given invalid code
        with pytest.raises(RatesNotAvailableError):
            c.get_rate('XYZ', 'CAD')


class TestConvert:

    def test_convert_valid_code(self):
        c = CurrencyRate()
        amount = 1500
        base = 'EUR'
        target = 'DKK'
        converted_amount = c.convert(base, target, amount)

        # Test that converted_amount is calculated correctly
        assert (converted_amount == round(Decimal(c.get_rate(base, target) * amount), 2))

    def test_convert_same_currency(self):
        c = CurrencyRate()
        amount = 1750
        base = 'CAD'
        target = 'CAD'
        converted_amount = c.convert(base, target, amount)

        # Test that converted_amount is the same as amount
        assert (converted_amount == Decimal(amount))

    def test_convert_invalid_code(self):
        c = CurrencyRate()
        amount = 20000
        base = 'USD'
        target = 'XYZ'

        with pytest.raises(RatesNotAvailableError):
            c.convert(base, target, amount)
