#! /usr/bin/python2.7

from urllib import urlopen

webpage = urlopen('http://www.python.org')

import re

text = webpage.read()

m = re.search('<a href="([^"]+)" .*?>about</a>', text, re.IGNORECASE)

print m.group(1)