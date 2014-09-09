#!/usr/bin/env python3

"""
CS313e: Quiz #2 (7 pts) [Fiona]
"""

""" ----------------------------------------------------------------------
 1. What is the output of the following?
    [Sec. 1.4, Pg. 12-13]
    (2 pts)

[2, 3, 2, 3, 2, 3]
[[2, 3], [2, 3], [2, 3]]
"""

a = [2, 3]
print([2, 3] * 3)
print([a]    * 3)

""" ----------------------------------------------------------------------
 2. What is the output of the following?
    [Sec. 1.4, Pg. 15]
    (2 pts)

6
4
"""

for v in range(6, 2, -2) :
    print(v)

""" ----------------------------------------------------------------------
 3. What is the output of the following?
    [Sec. 1.4, Pg. 42-53]
    (2 pts)

A.g
B.g
"""

class A :
    def f (self) :
        return self.g()

    def g (self) :
        return "A.g"

class B (A) :
    def g (self) :
        return "B.g"

print(A().f())
print(B().f())
