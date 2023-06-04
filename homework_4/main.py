import pprint

from flask import Flask
import sqlite3

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/order-price")
def order_price():
    query = "SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice * invoice_items.Quantity) " \
            "AS TOTAL FROM invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId " \
            "GROUP BY invoices.BillingCountry"
    records = execute_querry(query=query)
    pprint.pprint(records)
    return records


def execute_querry(query, args=()):
    with sqlite3.connect("homework_4/data_bases/chinook.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        records = cursor.fetchall()
    return records
