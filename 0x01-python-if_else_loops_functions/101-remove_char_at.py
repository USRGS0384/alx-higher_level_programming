#!/usr/bin/python3
# Author - Philip Ajuong Deng

"""Write a function that creates a copy of the string, removing
        removing the character at the position n
        (not the Python way, the “C array index”)."""


def remove_char_at(str, n):
    newStr = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            newStr += str[i]
    return newStr
