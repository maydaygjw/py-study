#! /usr/bin/python

for i, v in enumerate(['tic', 'tac', 'toe']):
	print i, v

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for i, v in knights.iteritems():
	print i, v

raw_data = list([56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8])

import math

new_data = [ data for data in raw_data if not math.isnan(data) ]
print new_data