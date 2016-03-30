#! /usr/bin/python2.7

f = open('somefile.txt', 'w')
f.write('Hello')
f.write('World')

f.close()

f = open('somefile.txt', 'r')
print f.read(4)
print f.read()


