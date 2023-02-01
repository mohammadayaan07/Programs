"""Write a Python program to extract specified number of elements from a given list, which follows each other continuously. 
	Original list:
	[1, 1, 3, 4, 4, 5, 6, 7]
	Extract 2 number of elements from the said list which follows each other continuously:
	[1, 4]
	Original lists:
	[0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
	Extract 4 number of elements from the said list which follows each other continuously:
	[4]"""
ls=[0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
a=[]
for i in range(len(ls)):
    if ls[i] in ls[i+1:]:
        a.append(ls[i])
print(set(a))
