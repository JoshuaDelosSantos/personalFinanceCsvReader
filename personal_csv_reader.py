"""

A simple Python script that reads from a CSV transaction export and writes to a file.

By: Joshua Delos Santos

Date started: 17/01/2024

"""

from datetime import datetime

CUSTOM_HEADERS = ['Date', 'Description', 'Debited', 'Credited']


def main():
    filename = input("CSV filename: ")
    data = load_data(filename)
    display_data(data)


def load_data(filename):
    """Load data from CSV file."""
    data = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip CSV header
        lines = in_file.readlines()

    for line in lines:
        parts = line.strip().split(',')
        date = datetime.strptime(parts[1], '%d/%m/%Y')

        try:
            debit_amount = float(parts[3])

        except ValueError:
            debit_amount = ''

        try:
            credit_amount = float(parts[4])

        except ValueError:
            credit_amount = ''

        data.append([date, parts[2], debit_amount, credit_amount])
        # Example:  Date, Description, Debit Amount, credit Amount

    return data


def save_data():
    pass


def sort_data():
    pass


def display_data(data):
    """"Display acquired data."""
    length_of_longest_string = max([len(datum[1]) for datum in data])

    print(f"{CUSTOM_HEADERS[0]:>10} | "
          f"{CUSTOM_HEADERS[1]:>{length_of_longest_string}} | "
          f"{CUSTOM_HEADERS[2]:7} | "
          f"{CUSTOM_HEADERS[3]:7}")

    for datum in data:
        print(f"{datum[0].date().strftime('%d/%m/%Y')} | "
              f"{datum[1]:{length_of_longest_string}} | "
              f"{datum[2]:7} | "
              f"{datum[3]:7} ")


def get_valid_filename():
    pass


if __name__ == '__main__':
    main()
