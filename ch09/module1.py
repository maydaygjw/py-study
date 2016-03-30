#! /usr/bin/python2.7 

import sys
sys.path.append('../')

import hello
import hello as hello1

hello1.print_world()

print hello1.__name__

from mypackage import module1
import mypackage.module2

module1.m1()
mypackage.module2.m2()

print dir(module1)
