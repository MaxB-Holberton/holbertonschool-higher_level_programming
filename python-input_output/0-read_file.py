#!/usr/bin/python3
"""
    Module for opening and reading a file
"""


def read_file(filename=""):
    """
        function for opening and reading a file
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
