#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args_list = sys.argv
    args_len = len(args_list)
    if (args_len == 1):
        print("0 arguments.")
    elif (args_len == 2):
        print("{} argument:".format(args_len - 1))
        for i in range(1, args_len):
            print("{}: {}".format(i, args_list[i]))
    else:
        print("{} arguments:".format(args_len - 1))
        for i in range(1, args_len):
            print("{}: {}".format(i, args_list[i]))
