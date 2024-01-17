"""

A simple Python script that reads from a CSV transaction export and writes to a file.

By: Joshua Delos Santos

Date started: 17/01/2024

"""


def main():
    filename = input("CSV filename: ")
    data = filename
    load_data(filename)


def load_data(filename):
    data = []
    with open(filename, 'r') as in_file:
        in_file.readline()  # Skip CSV header
        lines = in_file.readlines()

    for line in lines:
        parts = line.split(',')
        data.append([parts[1], parts[2], parts[3], parts[4], parts[5]])
        # Example:  Date, Description, Debit Amount, credit Amount, Balance

    return data


def save_data():
    pass


def sort_data():
    pass


def display_data():
    pass


def get_valid_filename():
    pass


if __name__ == '__main__':
    main()
