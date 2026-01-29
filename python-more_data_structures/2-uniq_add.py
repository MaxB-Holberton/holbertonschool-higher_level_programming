#!/usr/bin/python3

def uniq_add(my_list=[]):
    rtn_sum = 0
    if my_list:
        unique_list = list(set(my_list))

        for (i in unique_list):
            rtn_sum += i

    return (rtn_sum)
