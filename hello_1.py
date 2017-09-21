#! /usr/bin/env python3.6

import dis

import sys
sys.version
print(sys.version)
print()

a = 2
b = 4
a+b

def add(a, b):
    return a+b

dis.dis(add)
