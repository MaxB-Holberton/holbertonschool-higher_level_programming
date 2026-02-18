#!/usr/bin/python3
"""
    Module for printing pascal's triangle
"""


def pascal_triangle(n):
    """
        function for printing pascal's triangle
    """
    rtn_list = []
    if n <= 0:
        return rtn_list

    for i in range(n):
        new_line_list = []
        for j in range(i + 1):
            if j == 0 or j == (i):
                # the 0th and last item of the triangle are always 1
                new_line_list.append(1)
            else:
                # the triangle is the sum of items in the last row
                val_a = rtn_list[i - 1][j]
                val_b = rtn_list[i - 1][j - 1]
                new_line_list.append(val_a + val_b)

        rtn_list.insert(i, new_line_list)

    return rtn_list
