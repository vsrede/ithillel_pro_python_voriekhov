import csv
import requests

from faker import Faker
from flask import Flask, Response
from flask import request

from homework_3.utilities.csv_printer import csv_printer
from homework_3.utilities.symbol import symbol

# $env:FLASK_APP = "homework_3/main"
# flask run --no-debugger

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/students_list")
def generate_students():
    """def generate_students():
        # count should be as input GET parameter
        # first_name, last_name, email, password, birthday (18-60)
        # save to csv and show on web page
        # set limit as 1000
        pass
        *********************
    """
    fake = Faker()
    length_students_list = request.args.get("length", "100")

    if int(length_students_list) > 1000:
        return "ERROR: should be less than 1000"
    else:
        length_students_list = int(length_students_list)

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
    # fieldnames = ['first_name', 'last_name', 'email', 'password', 'date_of_birth']
    # with open(route_to_cvs, mode='w', newline='') as file:
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
    #     writer.writeheader()
    #
    #     for i in range(1, length_students_list):
    #         row_data = {
    #             'first_name': fake.first_name(),
    #             'last_name': fake.last_name(),
    #             'email': fake.email(),
    #             'password': fake.password(length=12),
    #             'date_of_birth': str(fake.date_of_birth(minimum_age=18, maximum_age=30))
    #         }
    #         writer.writerow(row_data)

    # df = pd.DataFrame.from_dict(list_students)
    # df.to_csv(r'homework_3/attachments/db_students.csv', index=False, header=True)

    return csv_printer(route_to_cvs)


@app.route("/bitcoin_value")
def get_bitcoin_value():
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
    currency = request.args.get("currency", "USD")
    convert = request.args.get("convert", "1")
    convert = int(convert)
    url = "https://bitpay.com/api/rates"
    list_currency_btc = requests.get(url, {})
    if list_currency_btc.status_code != 200:
        return Response("ERROR: Something went wrong", status=list_currency_btc.status_code)
    list_currency_btc = list_currency_btc.json()

    print(type(currency))
    print(type(list_currency_btc))
    value_currency = next((d for d in list_currency_btc if d.get('code') == currency), None)
    if convert == 1:
        result = f"Bitcoin exchange rate is {value_currency['rate']} {symbol(currency)}"
    else:
        result = f"Bitcoin exchange rate is {value_currency['rate']} {symbol(currency)}. " \
                 f"You need {value_currency['rate']*convert} {value_currency['name']}s for buy {convert} BTC"

    return result


