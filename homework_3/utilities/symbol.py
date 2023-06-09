import json
import requests


def symbol(currency):
    """
    The function takes a currency code and returns its symbol
    """
    resource_url = 'https://test.bitpay.com/currencies'
    headers = {'X-Accept-Version': '2.0.0', 'Content-type': 'application/json'}
    response = requests.get(url=resource_url, headers=headers).content
    decoded_response = json.loads(response.decode())
    decoded_response = decoded_response['data']
    value_currency = next((d for d in decoded_response if d.get('code') == currency), None)
    return value_currency["symbol"]
