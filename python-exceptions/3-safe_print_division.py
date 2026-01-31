#!/usr/bin/python3

def safe_print_division(a, b):
    rtn = 0
    try:
        rtn = a / b
    except:
        rtn = None
    finally:
        print("Inside result: {}".format(rtn))
        return(rtn)
