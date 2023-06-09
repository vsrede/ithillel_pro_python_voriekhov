import csv


def csv_printer(route_to_cvs):
    """
    The function takes the path to the cvs file and displays it on the screen
    """
    csv_lines = []
    with open(route_to_cvs, newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            csv_lines.append('_____'.join(row))
    return '<br>'.join(csv_lines)
