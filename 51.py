# Write a Python program to compute the difference between two lists.      
#Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
#Expected Output:
#Color1-Color2: ['white', 'orange', 'red']
#Color2-Color1: ['black', 'yellow']
from collections import Counter
c1=["red", "orange", "green", "blue", "white"]
c2=["black", "yellow", "green", "blue"]
a=Counter(c1)
b=Counter(c2)
c=a-b
print(c.keys())
