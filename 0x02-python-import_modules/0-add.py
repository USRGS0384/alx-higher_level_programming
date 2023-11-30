#!/usr/bin/python3
# Author - Philip Ajuong Deng

"""write a function that will import the value from the file add a and b."""


from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
