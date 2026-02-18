#!/usr/bin/python3
"""
    Module for writing to a file
"""


def append_write(filename="", text=""):
    """
        Function to write to a file
    """
    with open(filename, mode="a", encoding='utf-8') as f:
        return f.write(text)
