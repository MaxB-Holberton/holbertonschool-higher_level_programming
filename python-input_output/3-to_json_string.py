#!/usr/bin/python3
"""
    Module to convert python objects into JSON strings
"""


from json import dumps


def to_json_string(my_obj):
    """
    function to convert python objects into JSON strings
    """
    return dumps(my_obj)
