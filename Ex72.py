""" Write a Python program to remove consecutive duplicates of a given list. 
		Original list:
		[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
		After removing consecutive duplicates:
		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""
a=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
b=set(a)
print(list(b))