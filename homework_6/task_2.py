from flask import Flask
from webargs.flaskparser import use_kwargs
from webargs import fields

from homework_6.utilities.utilities import format_records, execute_querry

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>fd, Wld!</p>"


@app.route("/stats_by_city")
@use_kwargs(
    {
        "genre": fields.Str(required=True)
    },
    location="query"
)
def stats_by_city(genre):
    """Returns a city with a large number of purchases of the genre"""
    list_genres = "SELECT Name from genres"
    list_genres = execute_querry(query=list_genres)
    genre = genre.capitalize()

    if genre in format_records(list_genres):
        city = "SELECT customers.City, COUNT(*) AS ListensCount " \
               "FROM invoice_items " \
               "JOIN tracks ON invoice_items.TrackId = tracks.TrackId " \
               "JOIN genres ON tracks.GenreId = genres.GenreId " \
               "JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId " \
               "JOIN customers ON invoices.CustomerId = customers.CustomerId " \
               f"WHERE genres.Name = '{genre}'" \
               "GROUP BY customers.City " \
               "ORDER BY ListensCount DESC " \
               "LIMIT 1"

        city = execute_querry(query=city)
        return format_records(city)
    else:
        return "You genre incorrectly"
