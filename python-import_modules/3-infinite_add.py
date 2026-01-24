#!/usr/bin/python3
import sys

if __name__ == '__main__':
    args_list = sys.argv
    args_len = len(args_list)
    total = 0
    if (args_len == 1):
        print("{}".format(sum))
    else:
        for i in range(1, args_len):
            total += int(args_list[i])
        print(total)
