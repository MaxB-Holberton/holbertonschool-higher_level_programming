#!/usr/bin/env python3
"""
    Module with the function to convert csv to JSON
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """
        The conversion function
    """
    try:
        with open(csv_filename, mode='r', newline='') as csv_f:
            read_line = csv.DictReader(csv_f)
            dict_list = []
            for row in read_line:
                dict_list.append(row)

            with open("data.json", mode='w') as json_f:
                for item in dict_list:
                    json_f.write(json.dumps(item))

        return True

    except Exception as err:
        return False
