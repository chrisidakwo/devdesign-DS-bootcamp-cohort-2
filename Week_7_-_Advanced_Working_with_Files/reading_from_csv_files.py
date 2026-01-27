import csv
from pprint import pprint

FILENAME = "files/house_prices.csv"

def read_csv_file(file_path):
    """Read the content of a CSV file using the Python in-built csv module"""

    with open(file_path, "r") as file:
        # The first thing you do in order to read the content of a CSV/Excel file is to instantiate/create
        # a new instance of the CSV reader
        csv_reader = csv.reader(file)

        print("\nROWS IN DATA FILE")
        print("")
        for row in csv_reader:
            print(row) # row is a list of values
            print("")

def read_csv_file_dict(file_path):
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        print("\nROWS IN DATA FILE")
        print("")
        for row in csv_reader:
            pprint(row) # row is a dictionary {column_name: value}
            print("") 


read_csv_file(FILENAME)
print("\n===================================\n")
read_csv_file_dict(FILENAME)
