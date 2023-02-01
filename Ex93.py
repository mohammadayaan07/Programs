"""Write a Python program to count the number of sublists contain a particular element. 
		Original list:
		[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
		Count 1 in the said list:
		3
		Count 7 in the said list:
		2
		Original list:
		[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
		Count 'A' in the said list:
		3
		Count 'E' in the said list:
		1"""
lst=[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
try:
    a=int(input("enter the number you check:"))
    c=0
    for i in lst:
        if a in i:
            c+=1
    print(c)
except ValueError:
    print("dont enter the str sepical char")