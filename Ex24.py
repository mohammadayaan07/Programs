#Write a Python program to append a list to the second list
lst=[12,13,14,15]
lst1=[120,130,140,150]
for i in range(len(lst1)):
    lst.append(lst1[i])
print(lst)