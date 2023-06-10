import sqlite3


def format_records(records: list) -> str:
    """
     The function takes a list and returns that list formatted
    """
    return "<br><br>".join(str(records) for records in records)


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