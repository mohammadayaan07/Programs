#Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user. 
"""	Input rows: 2
	Input columns: 2
	Input number of elements in a row (1, 2, 3):
	1 2
	3 4
	sum for each column:
	4 6"""
lst=[]
for i in range(2):
    x=[]
    for j in range(2):
        n=int(input("enter the num:"))
        x.append(n)
    lst.append(x)
print(lst[0][0])
print(lst[1][0])