#Write a Python program to find the second smallest number in a list. 
lst=[12,45,67,90,100,1,2]
"""sml=lst[0]
for i in range(len(lst)):
    if sml>lst[i]:
        sml=lst[i]
lst.remove(sml)
sml=lst[0]
for i in range(len(lst)):
    if sml>lst[i]:
        sml=lst[i]
print(sml)
"""
lst.sort()
print(lst[1])
print(lst[-2])