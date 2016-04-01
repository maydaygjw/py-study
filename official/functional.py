#! /usr/bin/python

def f(x): return x % 3 == 0 or x % 5 == 0
def cube(x): return x * x * x
def add(x, y): return x + y

print filter(f, range(2, 25))
print map(cube, range(1, 1))

print map(add, range(8), range(8))
print reduce(add, range(1, 11))