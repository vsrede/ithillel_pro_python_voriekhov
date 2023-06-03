"""def generate_students():
    # count should be as input GET parameter
    # first_name, last_name, email, password, birthday (18-60)
    # save to csv and show on web page
    # set limit as 1000
    pass
    *********************
"""
import csv
from flask import Flask
from flask import request
from faker import Faker

# $env:FLASK_APP = "homework_3/main"
# flask run --no-debugger

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/students_list")
def generate_students():
    fake = Faker()
    length_students_list = request.args.get('length', '100')

    if int(length_students_list) > 1000:
        return "ERROR: should be less than 1000"
    else:
        length_students_list = int(length_students_list)

    route_to_cvs = "homework_3/attachments/db_students.csv"
    # dictionary_students = {}
    # for i in range(1, length_students_list):
    #      dictionary_students[i] = {
    #         'fname': fake.first_name(),
    #         'lname': fake.last_name(),
    #         'email': fake.email(),
    #         'pass': fake.password(length=12),
    #         'dob': str(fake.date_of_birth(minimum_age=18, maximum_age=30))
    #     }
    fieldnames = ['first_name', 'last_name', 'email', 'password', 'date_of_birth']
    with open(route_to_cvs, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for i in range(1, length_students_list):
            row_data = {
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': fake.email(),
                'password': fake.password(length=12),
                'date_of_birth': str(fake.date_of_birth(minimum_age=18, maximum_age=30))
            }
            writer.writerow(row_data)

    # df = pd.DataFrame.from_dict(dictionary_students)
    # df.to_csv(r'homework_3/attachments/db_students.csv', index=False, header=True)

    return csv_printer(route_to_cvs)


def csv_printer(route_to_cvs):
    csv_lines = []
    with open(route_to_cvs, newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            csv_lines.append('_____'.join(row))
    return '<br>'.join(csv_lines)

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



