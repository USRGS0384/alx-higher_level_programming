#!/usr/bin/python3
# Author - Philip Ajuong Deng

import sys
import hidden_4 as hidden

if __name__ != "__main__":
    exit()

for name in dir(hidden):
    if name[0:2] != "__":
        print(name)
