#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            upper = ord(char) - 32
            upper = chr(upper)
        else:
            upper = char
        print("{}".format(upper), end="")
    print()