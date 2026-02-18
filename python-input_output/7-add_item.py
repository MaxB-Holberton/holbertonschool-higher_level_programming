#!/usr/bin/python3
import sys
import os

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""
    Module to read and write to json files
"""

filename = "add_item.json"

if os.path.exists(filename):
    file_f = load_from_json_file(filename)
else:
    file_f = []

for i in range(1, len(sys.argv)):
    file_f.append(sys.argv[i])

save_to_json_file(file_f, filename)
