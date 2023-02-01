#Write a Python program to get the frequency of the elements in a list. 
lst=['a','a','b','c','c','b','d','d','d']
feq={}
for item in lst:
    if item in feq:
        feq[item]+=1
    else:
        feq[item]=1
print(feq)

print("*"*40)

import collections
lst2=['a','a','b','c','c','b','d','d','d']
feq1=collections.Counter(lst2)
print(dict(feq1))
