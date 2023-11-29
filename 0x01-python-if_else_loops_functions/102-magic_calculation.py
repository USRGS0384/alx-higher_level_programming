#!/usr/bin/python3
#Author - Philip Ajuong Deng

"""Write the Python function def magic_calculation(a, b, c)
    that does exactly the same as the Python bytecode does."""

def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b

    return a * b - c
