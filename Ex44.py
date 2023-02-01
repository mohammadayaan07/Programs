# Write a Python program to generate groups of five consecutive numbers in a list. 
lst=[]
n=int(input("enter the number:"))
for i in range(n,n+5):
    lst.append(i)
print(lst)