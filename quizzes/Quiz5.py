#!/usr/bin/env python3

"""
CS313e: Quiz #5 (7 pts) [Prateek]
"""

""" ----------------------------------------------------------------------
 1. For the anagram detection problem, what were the best complexities of
    the following two approaches?
    [Sec. 2.2, Pg. 66-70]
    (2 pts)

    a. sort  and compare
    b. count and compare

O(n log n)
O(n)
"""

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    (2 pts)

[2, 3, 4, 5, 6]
"""

def f (x) :
    x += [5, 6]

a = [2, 3, 4]
f(a)
print(a)

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    (2 pts)

(2, 3, 4)
"""

def g (x) :
    x += (5, 6)

a = (2, 3, 4)
g(a)
print(a)
