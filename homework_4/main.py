import pprint

from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args
import sqlite3

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


args_parser = {
    "country": fields.Str(missing="all")
}


@app.route("/order-price")
@use_args(args_parser, location="query")
def order_price(args):
    """# UnitPrice * Quantity - sales.
    # Calculate sales
    # Add possibility to get sum of sales data by Country
    # by default all countries
    # join two tables invoices and invoices_items
    pass
    # show sales by country on page / if no country show all sales by all counties."""
    country = args['country']
    if country == "all":
        query = "SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice * invoice_items.Quantity) " \
                "AS TOTAL FROM invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId " \
                "GROUP BY invoices.BillingCountry"
    else:
        query = "SELECT invoices.BillingCountry, SUM(UnitPrice * Quantity) " \
                "AS TOTAL FROM invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId " \
                f"WHERE invoices.BillingCountry = {country}" \
                "GROUP BY invoices.BillingCountry"
    records = execute_querry(query=query)
    pprint.pprint(records)
    return format_records(records)


def execute_querry(query, args=()):
    """
    The function takes an SQL command and returns the result from the database
    """
    with sqlite3.connect("homework_4/data_bases/chinook.db") as connection:
        cursor = connection.cursor()
        cursor.execute(query, args)
        connection.commit()
        records = cursor.fetchall()
    return records


def format_records(records: list) -> str:
    """
     The function takes a list and returns that list formatted
    """
    return "<br>".join(str(records) for records in records)