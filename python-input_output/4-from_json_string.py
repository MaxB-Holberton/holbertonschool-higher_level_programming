#!/usr/bin/python3
from json import loads
"""
    Module to convert JSON strings to python objects
"""


def from_json_string(my_str):
    """
        function to convert JSON strings to python objects
    """
    return loads(my_str)
