import csv


def read_csv(csv_filename):
    """
    Build a list of dictionaries from a CSV file without converting numeric
    values into integers.

    :param csv_filename: the name of the CSV file to read
    :return: list of field names (column headers in the CSV file) and
    list of dictionaries holding the data (one dictionary for each row)
    """
    data_in = open(csv_filename, 'r')
    csv_reader = csv.DictReader(data_in)
    fields = csv_reader.fieldnames

    table = []
    for rowDict in csv_reader:
        table.append(rowDict)
    data_in.close()

    return fields, table


def print_table(table, fields, width=20):
    """
    Given a table that is a list of dictionaries, and a list of strings
    containing the fields and the order in which to print them, this prints
    the field titles, then the rows of the table, giving each field the input
    number of characters.
    """
    # print header
    header_row = ""
    for f in fields:
        print_f = f[:width].center(width)
        header_row += print_f + ' '
    print(header_row)

    # loop over rows
    for row in table:

        # print current row
        row_string = ""
        for f in fields:
            val = row[f]
            print_val = str(val)
            print_val = print_val[:width].center(width)
            row_string += print_val + ' '
        print(row_string)

field_names, sun_table = read_csv("../DataFiles/sunRiseSet.csv")
print(field_names)
print(sun_table[0])  # printing just the first row of data
print_table(sun_table, field_names, 15)

def lookup_phone(name, direct_table):
    """
    Given a name and a list-of-dictionaries,look up the person's phone number
    :param name:
    :param direct_table:
    :return:
    """
    for row in direct_table:
        if row['Name'] == name:
            return row['Phone']

    return "No entry: " + name
