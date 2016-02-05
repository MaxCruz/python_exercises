#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibonacci(n):
        print ""
        a, b = 0, 1
        for i in range(n):
            print a,
            a, b = b, a + b

print """
The fibonacci sequence starts with 0 and 1, each subsequent number is the sum of the previous two.
This example iterates the sequence to the desired number.
"""

number= int(raw_input("Number of iterations:  "))
fibonacci(number)