#! /usr/bin/python2.7

def print_params(*params):
	print params

def print_params2(title, *params):
	print title
	print params

def print_params3(**params):
	print params

print_params('Testing')
print_params(1, 2, 3)

print_params2('Params: ', 1, 2, 3)
print_params2(title = 'Nothing')

print_params3(x = 1, y = 2, z = 3)

def add(a, b): return a + b

print add(1, 2)