#!/usr/bin/python3
from json import dumps

"""
    Module to convert python objects into JSON strings
"""


def to_json_string(my_obj):
    """
    function to convert python objects into JSON strings
    """
    return dumps(my_obj)
