# Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space. 
"""	Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
	Minimum value: 4
	Maximum value: 22
	Result:
	20 25 45 55 60 70 80 90 110"""
lst=[22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
new=sorted(lst)
print(new)
print("min",new[0])
print("max",new[-1])
ab=[]
for i in new:
    a=i*5
    ab.append(a)
print(ab)