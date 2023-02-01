#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 

lst=[]
for val in range(2,30):
    ls=(val**2)
    lst.append(ls)
print(lst)
print(lst[0:5]+lst[-5:])