#!/usr/bin/python3
# Author - Philip Ajuong Deng

def uppercase(str):
    for uppercase in range(len(str)):

        char = ord(str[uppercase])
        if char >= 97 and char <= 122:
            char = char - 32
        print("{}".format(chr(char)), end="")
    print()
