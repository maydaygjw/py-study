#! /usr/bin/python
import json

print json.dump([1, '2', 3], open('my.json', 'rw'))


