#Write a Python program to get the difference between the two lists. 
lst=[1,20,3,4]
lst1=[12,13,14,15]
lst2=[]
for i in range(len(lst1)):
    ls=lst[i]-lst1[i]
    lst2.append(ls)
print(lst2)