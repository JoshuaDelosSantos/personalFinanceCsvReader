"""

A simple Python script that reads from a CSV transaction export and writes to a file.

By: Joshua Delos Santos

Date started: 17/01/2024

"""

import os
from datetime import datetime
from operator import itemgetter

CUSTOM_HEADERS = ['Date', 'Description', 'Debited', 'Credited']


def main():
    filename = get_valid_filename()
    data = load_data(filename)
    data.sort(key=itemgetter(0, 1))
    display_data(data)
    # save_data(data)


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


def save_data(data):
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
    """Get a valid filename from the user."""
    is_valid_filename = False
    while not is_valid_filename:
        try:
            script_directory = os.path.dirname(os.path.abspath(__file__))
            filename = input('CSV filename: ')
            full_path = os.path.join(script_directory, filename)

            if os.path.isfile(full_path):
                is_valid_filename = True
            else:
                print("File not found. Please enter a valid filename.")
        except Exception as e:
            print(f"An error occurred: {e}")

    return full_path


if __name__ == '__main__':
    main()
