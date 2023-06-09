from flask import Flask
from webargs import fields, validate
from webargs.flaskparser import use_kwargs
from homework_4.utilities.utilities import format_records, execute_querry
# $env:FLASK_APP = "homework_4/main"
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/order-price")
@use_kwargs(
    {
        "country": fields.Str(missing="")
    },
    location="query"
)
def order_price(country):
    """# UnitPrice * Quantity - sales.
        # Calculate sales
        # Add possibility to get sum of sales data by Country
        # by default all countries
        # join two tables invoices and invoices_items
        pass
        # show sales by country on page / if no country show all sales by all counties."""
    if country == "":
        query = "SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice * invoice_items.Quantity) " \
                "AS TOTAL FROM invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId " \
                "GROUP BY invoices.BillingCountry"
    else:
        query = "SELECT invoices.BillingCountry, SUM(UnitPrice * Quantity) " \
                "AS TOTAL FROM invoice_items JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId " \
                f"WHERE invoices.BillingCountry = {country}" \
                "GROUP BY invoices.BillingCountry"
    records = execute_querry(query=query)
    return format_records(records)


@app.route("/get-all-info-about-track")
@use_kwargs(
    {
        "track_id": fields.Int(missing=1, validate=lambda val: val < 10)
    },
    location="query"
)
def get_all_info_about_track(track_id):
    """
        # join all possible tables and show all possible info about all tracks
        # as input track ID
    """
    query = "SELECT * FROM tracks " \
            "JOIN playlist_track ON playlist_track.TrackId = tracks.TrackId " \
            "JOIN playlists ON playlists.PlaylistId = playlist_track.PlaylistId " \
            "JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId " \
            "JOIN genres ON genres.GenreId = tracks.GenreId " \
            "JOIN albums ON albums.AlbumId = tracks.AlbumId " \
            "JOIN artists ON artists.ArtistId = albums.ArtistId " \
            "JOIN invoice_items ON invoice_items.TrackId=tracks.TrackId " \
            "JOIN invoices ON invoices.InvoiceId = invoice_items.InvoiceId " \
            "JOIN customers ON customers.CustomerId = invoices.CustomerId " \
            f"WHERE tracks.TrackId = {track_id}"
    result = execute_querry(query=query)
    return format_records(result)


@app.route("/get_all_info_about_track")
def get_times_info_about_track():
    """
        # show time of all tracks of all albums in hours
        # use info about all tracks
    """
    query = "SELECT albums.Title, SUM(tracks.Milliseconds)/3600000.0 AS TOTAL " \
            "FROM albums JOIN tracks ON tracks.AlbumId = albums.AlbumId GROUP BY albums.Title"
    result = execute_querry(query=query)
    return result
