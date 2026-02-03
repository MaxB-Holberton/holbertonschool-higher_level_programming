#!/usr/bin/python3
"""
    Adds newlines to text after specific characters
"""
def text_indentation(text):
    """
        Adds newlines to text after specific characters

        Arguments:
            text (str): text to print
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    t_bool = False
    for i in text:
        if t_bool == False:
            print(i, end="")

        if t_bool == True:
            if i != ' ':
                print(i, end="")
            t_bool = False

        if i == '.' or i =='?' or i ==':':
            print('\n')
            t_bool = True
