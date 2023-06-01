"""
for run your need write: $env:FLASK_APP = "homework_2/main"
"""


from flask import Flask
import string
import pandas as pd
from random import choice, randint

app = Flask(__name__)


@app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
def get_password():
    pass_len = randint(10, 20)
    value_pass = [*string.ascii_lowercase,
                  *string.ascii_uppercase,
                  *string.digits,
                  *string.punctuation]
    password = ''.join([choice(value_pass) for _ in range(pass_len)])
    return password


@app.route("/average")
def calculate_average():
    data_lst = pd.read_csv('homework_2/processing/hw.csv')
    average_height = round((data_lst["Height(Inches)"]).sum() / data_lst.iloc[-1]["Index"])
    average_weight = round((data_lst["Weight(Pounds)"]).sum() / data_lst.iloc[-1]["Index"])

    return (f"Average height = {average_height} inches, average weight = {average_weight} pounds")



