#!/usr/bin/python3
# Athor - Philip Ajuong Deng

""""Print the alphabet in reverse order alternating upper- and lower-case."""

for number in range(122, 96, -1):
    if number % 2 == 0:
        n = chr(number)
    else:
        n = chr(number-32)
    print("{}".format(n), end="")
