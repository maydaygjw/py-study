#! /usr/local/bin/python

database = [
	['albert', '1234'],
	['smith', '7524'],
	['john', '3838']
]

username = input('Enter your username: ')
pincode = input('Enter your pincode: ')

if([username, pincode] in database):
	print("Access Granted")

