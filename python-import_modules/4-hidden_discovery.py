#!/usr/bin/python3
import hidden_4 as h4

items = dir(h4)
for i in range(len(items)):
	if items[i][:2] != '__':
		print(items[i])
