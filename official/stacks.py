#! /usr/bin/python

stack = [3, 4, 5]
stack.append(6)
stack.append(7)

print stack

stack.pop()
stack.pop()

print stack

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print queue

print queue.popleft()
print queue.pop()

print queue