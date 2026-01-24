#!/usr/bin/python3
import hidden_4 as h4

if __name__ == '__main__':
    items = dir(h4)
    for i in range(len(items)):
        if items[i][:2] != '__':
            print(items[i])
