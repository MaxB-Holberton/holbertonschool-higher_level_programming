#!/usr/bin/python3

def no_c(my_string):
    return_string = ""
    for idx in my_string:
        if idx != 'c' and idx != 'C':
            return_string += idx

    return (return_string)
