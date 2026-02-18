#!/usr/bin/python3
from json import loads
"""
    Module to convert JSON strings to python objects
"""


def load_from_json_file(filename):
    with open(filename, mode="r", encoding='utf-8') as f:
        return loads(f.read())
