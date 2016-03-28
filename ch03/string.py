#! /usr/local/bin/python

import math

print('%s plus %s equals %s' % (1, 1, 2))

print('Pi with three decimals: %.3f' % math.pi)

print('Price of eggs: $%d' % 42)

print('Hexadecimal price of eggs: %x' % 42)

seq = 'aaa', 'bbb', 'ccc'
seq2 = ['aaa', 'bbb', 'ccc']
seq3 = ['aaa', 'bbb', 'ccc']
sep = "+"

print(seq == seq2)
print(seq3 == seq2)

print(sep.join(seq))

