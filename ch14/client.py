#! /usr/bin/python2.7

import socket

s = socket.socket()

host = socket.gethostname()
port = 1234

s.connect((host, port))

print s.recv(1234)