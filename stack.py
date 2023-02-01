"""colletions module in stack 
collections.deque() to making an  empty list of stck 
queue function in to create stack also as get() and put()
import queue  and
queue.LifoQueue(range)"""
import collections
stack=collections.deque()
print(stack)
stack.append(10)
print(stack)
stack.pop()
print(stack)
print(not stack)


import queue 
stack =queue.LifoQueue()
stack.put(10)
print(stack.get())