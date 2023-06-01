"""def generate_students():
    # count should be as input GET parameter
    # first_name, last_name, email, password, birthday (18-60)
    # save to csv and show on web page
    # set limit as 1000
    pass
    *********************
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
# $env:FLASK_APP = "homework_3/main"

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/students_list")
def generate_students():
    length_students_list = request.args.get('length', '100')
    if int(length_students_list) > 1000:
        return "ERROR: should be less than 1000"
    else:
        length_students_list = int(length_students_list)

    return str(length_students_list)