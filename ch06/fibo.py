#! /usr/local/bin/python

fibs = [1, 1]

for i in range(8): 
	fibs.append(fibs[-1] + fibs[-2])

print(fibs)