#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple_a = tuple_check(tuple_a)
    new_tiple_b = tuple_check(tuple_b)

    return ((new_tuple_a[0] + new_tiple_b[0], new_tuple_a[1] + new_tiple_b[1]))


def tuple_check(t_check=()):
    if (len(t_check) == 0):
        return ((0, 0))

    elif (len(t_check) == 1):
        return ((t_check[0], 0))

    elif (len(t_check) > 2):
        return ((t_check[0], t_check[1]))

    return (t_check)
