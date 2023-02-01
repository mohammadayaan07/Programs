#Write a Python program to insert an element at a specified position into a given list. 
"""	Original list:
	[1, 1, 2, 3, 4, 4, 5, 1]
	After inserting an element at kth position in the said list:
	[1, 1, 12, 2, 3, 4, 4, 5, 1]
"""
lst=[1, 1, 2, 3, 4, 4, 5, 1]
i=int(input("    "))
val=int(input(""))
lst[i]=val
print(lst)