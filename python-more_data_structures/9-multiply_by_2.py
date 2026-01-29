#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary:
        dict_list = list(a_dictionary.keys())
        for key in dict_list:
            new_dict[key] = a_dictionary[key] * 2

    return (new_dict)
