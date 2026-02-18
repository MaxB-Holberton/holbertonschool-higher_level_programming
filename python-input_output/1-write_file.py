#!/usr/bin/python3
"""
    Module for writing to a file
"""


def write_file(filename="", text=""):
    """
        Function to write to a file
    """
    with open(filename, mode="w", encoding='utf-8') as f:
        return f.write(text)
