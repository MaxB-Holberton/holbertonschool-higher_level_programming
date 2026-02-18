#!/usr/bin/python3
"""
    Module to read json string from a file
"""

from json import loads


def load_from_json_file(filename):
    """
        read from a json file
    """
    with open(filename, mode="r", encoding='utf-8') as f:
        return loads(f.read())
