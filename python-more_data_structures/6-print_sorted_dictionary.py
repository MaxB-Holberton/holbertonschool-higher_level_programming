#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        dict_list = list(a_dictionary.keys())
        dict_list.sort()

        for item in dict_list:
            print("{}: {}".format(item, a_dictionary.get(item)))
