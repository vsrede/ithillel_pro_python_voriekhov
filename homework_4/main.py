from flask import Flask
from webargs import fields
from webargs.flaskparser import use_args

from homework_4.utilities.utilities import format_records, execute_querry

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


args_parser = {
    "country": fields.Str(missing="all"),
    "track_id": fields.Str(missing='1')
}


@app.route("/order-price")
@use_args(args_parser, location="query")
def order_price(args_parser):
    """# UnitPrice * Quantity - sales.
        # Calculate sales
        # Add possibility to get sum of sales data by Country
        # by default all countries
        # join two tables invoices and invoices_items
        pass
        # show sales by country on page / if no country show all sales by all counties."""
    country = args_parser['country']
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
    return format_records(records)


@app.route("/get-all-info-about-track")
@use_args(args_parser, location="query")
def get_all_info_about_track(args_parser, location="query"):
    """
        # join all possible tables and show all possible info about all tracks
        # as input track ID
    """
    track_id = int(args_parser["track_id"])
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


