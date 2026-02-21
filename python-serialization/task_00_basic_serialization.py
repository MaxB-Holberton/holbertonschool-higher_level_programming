#!/usr/bin/env python3
"""
	functions to serialize and deserialize json strings
"""


from json import loads, dumps


def serialize_and_save_to_file(data, filename):
	with open(filename, mode="w", encoding='utf-8') as f:
		f.write(dumps(data))


def load_and_deserialize(filename):
	with open(filename, mode="r", encoding='utf-8') as f:
		return(loads(f.read()))
