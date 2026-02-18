#!/usr/bin/python3
"""
    Module to convert JSON strings to python objects
"""


from json import loads


def from_json_string(my_str):
    """
        function to convert JSON strings to python objects
    """
    return loads(my_str)
