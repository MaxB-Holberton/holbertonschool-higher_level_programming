#!/usr/bin/python3
from json import dumps
"""
    Module to write to a file
"""


def save_to_json_file(my_obj, filename):
    """
        Function to write an object to json file
    """
    with open(filename, mode="w", encoding='utf-8') as f:
        return f.write(dumps(my_obj))
