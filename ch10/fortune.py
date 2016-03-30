#! /usr/bin/python2.7

import fileinput, random

fortunes = list(fileinput.input())

print random.choice(fortunes)