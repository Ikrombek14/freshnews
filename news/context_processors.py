from .views import get_currency_rates

def currency_rates(request):
    rates = get_currency_rates()
    return rates