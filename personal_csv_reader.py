"""

A simple Python script that reads from a CSV transaction export and writes to a file.

By: Joshua Delos Santos

Date started: 17/01/2024

"""

import os
from operator import attrgetter
from line import Line

CUSTOM_HEADERS = ['Date', 'Description', 'Debited', 'Credited', 'Category']


# CATEGORY_TO_TEXTS = {
#     'Grocery': ['WOOLWORTHS', 'COLES'],
#     'Travel': ['AIRBNB', 'HOTEL', 'GRAB', 'FOREIGN FEE'],
#     'Dining': ['RESTAURANT', 'CAFE', 'FOOD', 'EATERY', 'MCDONALDS', 'SUSHI'],
#     'Shopping': ['KMART', 'SHOP', 'CLOTHING', 'RETAIL', 'MARKET'],
#     'Utilities': ['BILL', 'OPTUS', 'TELSTRA'],
#     'Salary': ['SALARY', 'PAYROLL', 'PAYMENT', 'DEPOSIT'],
#     'Entertainment': ['NETFLIX', 'SPOTIFY', 'STREAMING', 'MOVIE'],
#     'Health and Fitness': ['GYM', 'FITNESS', 'WORKOUT'],
#     'Transfer': ['TRANSFER', 'TFR', 'PAYMENT TO'],
#     'Other': ['PAYMENT BY AUTHORITY', 'WITHDRAWAL ONLINE', 'DEPOSIT-OSKO PAYMENT', 'WITHDRAWAL-OSKO PAYMENT']
# }


def main():
    filename = get_valid_filename()
    data = load_data(filename)
    data.sort(key=attrgetter('date', 'description'))
    display_data(data)
    # save_data(data, filename)
    print(f"{len(data)} entries recorded.")
    print("Done!")


def load_data(filename):
    """Load data from CSV file."""
    data = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip CSV header
        lines = in_file.readlines()

    for line in lines:
        parts = line.strip().split(',')

        try:
            debit_amount = float(parts[3])

        except ValueError:
            debit_amount = ''

        try:
            credit_amount = float(parts[4])

        except ValueError:
            credit_amount = ''

        data.append(Line(parts[1], parts[2], debit_amount, credit_amount))
        # Example:  Date, Description, Debit Amount, credit Amount

    return data


def save_data(data, filename):
    """Save data to file."""
    with open(f"modified_{filename}", 'w') as out_file:
        print(",".join([header for header in CUSTOM_HEADERS]), file=out_file)

        for datum in data:
            date = datum[0].date().strftime('%d/%m/%Y')
            debited = str(datum[2])
            credited = str(datum[3])
            category = determine_category(datum[1])
            print(f"{date},{datum[1]},{debited},{credited},{category}", file=out_file)


def display_data(data):
    """"Display acquired data."""
    for line in data:
        print(f"{line} {line.determine_category()}")


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

    return filename


if __name__ == '__main__':
    main()
