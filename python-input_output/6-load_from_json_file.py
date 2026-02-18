#!/usr/bin/python3
"""
    Module to convert JSON strings to python objects
"""

from json import loads


def load_from_json_file(filename):
    with open(filename, mode="r", encoding='utf-8') as f:
        return loads(f.read())
