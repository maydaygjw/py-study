#! /usr/bin/python2.7

from heapq import *
from random import shuffle

data = range(10)

shuffle(data)

heap = []

for n in data:
	heappush(heap, n)

print heap
heappush(heap, 0.5)

print heap

print heappop(heap)
print heappop(heap)
print heappop(heap)