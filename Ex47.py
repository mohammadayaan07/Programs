#47. Write a Python program to insert an element before each element of a list.
eml=12
lst=[120,130,140,150]
lst1=[]
for i in range(len(lst)):
    lst1.append(lst[i])
    lst1.append(eml)
print(lst1)