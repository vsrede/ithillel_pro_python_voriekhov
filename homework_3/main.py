import csv

import requests

from faker import Faker
from flask import Flask
from webargs import fields
from webargs.flaskparser import use_kwargs
from homework_3.utilities.csv_printer import csv_printer
from homework_3.utilities.symbol import symbol

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/students_list")
@use_kwargs(
    {
        "length_students_list": fields.Int(missing=1, validate=lambda val: val < 1000)
    },
    location="query"
)
def generate_students(length_students_list):
    """def generate_students():
        # count should be as input GET parameter
        # first_name, last_name, email, password, birthday (18-60)
        # save to csv and show on web page
        # set limit as 1000
        pass
        *********************
    """
    fake = Faker()
    route_to_cvs = "homework_3/attachments/db_students.csv"
    list_students = []
    csv_columns = ["first_name", "last_name", "email", "password", "date_of_birth"]
    for i in range(1, length_students_list):
        student = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "password": fake.password(length=12),
            "date_of_birth": str(fake.date_of_birth(minimum_age=18, maximum_age=30))
        }

        list_students.append(student)

    with open(route_to_cvs, "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        writer.writerows(list_students)

    return csv_printer(route_to_cvs)


@app.route("/bitcoin_value")
@use_kwargs(
    {
        "currency": fields.Str(missing="USD"),
        "convert": fields.Int(missing=1, validate=lambda val: val < 1000)

    },
    location="query"
)
def get_bitcoin_value(currency, convert):
    """
        def get_bitcoin_value():
        # https://bitpay.com/api/rates
        # /bitcoin_rate?currency=UAH&convert=100
        # input parameter currency code
        # default is USD
        # return value currency of bitcoin
        # * https://bitpay.com/api/
        # * return symbol of input currency code
        # * add one more input parameter count and multiply by currency (int)
        pass
        """
    url = "https://bitpay.com/rates/" + currency
    list_currency_btc = requests.get(url, {}).json()
    value_currency = list_currency_btc['data']['rate']
    if convert == 1:
        result = f"Bitcoin exchange rate is {value_currency} {symbol(currency)}"
    else:
        result = f"Bitcoin exchange rate is {value_currency} {symbol(currency)}. " \
                 f"You need {value_currency * convert}, {currency} for buy {convert} BTC"

    return result
