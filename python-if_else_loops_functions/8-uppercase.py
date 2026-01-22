#!/usr/bin/python3
def uppercase(str):
	upper_str = ""
	for i in range(len(str)):
		char = ord(str[i])
		if (char > 96 and char < 123):
			upper_str += chr(char - 32)
		else:
			upper_str += str[i]
	print(upper_str)

