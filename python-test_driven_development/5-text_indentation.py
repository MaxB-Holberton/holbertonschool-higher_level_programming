#!/usr/bin/python3

def text_indentation(text):
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    t_bool = False
    for i in text:
        if t_bool == False:
            print(i, end="")

        if t_bool == True:
            t_bool = False

        if i == '.' or i =='?' or i ==':':
            print('\n')
            t_bool = True
