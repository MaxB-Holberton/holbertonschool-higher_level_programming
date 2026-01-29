#!/usr/bin/python3

def convert_input(i):
    if i == 'M':
        return (1000)
    elif i == 'D':
        return (500)
    elif i == 'C':
        return (100)
    elif i == 'L':
        return (50)
    elif i == 'X':
        return (10)
    elif i == 'V':
        return (5)
    elif i == 'I':
        return (1)
    else:
        return (0)

def roman_to_int(roman_string):
    if roman_string == None:
        return (0)
    #if not string return 0
    else:
        rtn = 0
        last = roman_string[0]
        sign = True
        for i in roman_string:
            num = convert_input(i)
            if i != last:
                #if the sign changes -> check if it's bigger or smaller
                if num > convert_input(last):
                    sign = sign ^ True
                else:
                    sign = True

            if sign:
                rtn += num
            else:
                rtn += num - (convert_input(last) * 2)

            last = i

    return (rtn)
