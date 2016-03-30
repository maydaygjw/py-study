#! /usr/bin/python2.7

mySet = []

for i in range(5):
	mySet.append(set(range(i, i+5)))

print mySet

print reduce(set.union, mySet)
