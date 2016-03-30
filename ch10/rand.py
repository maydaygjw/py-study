#! /usr/bin/python2.7

from random import *
from time import *

date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)

randtime = uniform(time1, time2)

print asctime(localtime(randtime))