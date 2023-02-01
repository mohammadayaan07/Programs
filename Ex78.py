#Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
# Original list:
"""	[1, 1, 2, 3, 4, 4, 5, 1]
	Length of the first part of the list: 3
	Splited the said list into two parts:
	([1, 1, 2], [3, 4, 4, 5, 1])"""
lst=[1, 1, 2, 3, 4, 4, 5, 1]
n=int(input("enter n:"))
lst1=lst[0:n] 
lst2=lst[n:]
tp=(lst1,lst2)
print(tp)
