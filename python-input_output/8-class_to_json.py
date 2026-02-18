#!/usr/bin/python3

"""
    Module for returning a dictionary as a JSON string
"""


def class_to_json(obj):
    """
        Class for returning a disctionary as a JSON string
    """
    return obj.__dict__
