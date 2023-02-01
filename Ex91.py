#Write a Python program to find the list with maximum and minimum length. 
"""	Original list:
	[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
	List with maximum length of lists:
	(3, [13, 15, 17])
	List with minimum length of lists:
	(1, [0])
	Original list:
	[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
	List with maximum length of lists:
	(3, [3, 5, 7])
	List with minimum length of lists:
	(1, [0])
	Original list:
	[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
	List with maximum length of lists:
	(4, [1, 34, 5, 7])
	List with minimum length of lists:
	(1, [12])"""
lst=[[0], [1, 3], [5,6,8,9,10, 7], [13, 15, 17], [9, 11],[90,68,9,9]]
lst=sorted(lst)
print("min=",lst[0])
print("max=",lst[-1])
