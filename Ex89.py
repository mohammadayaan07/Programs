#Write a Python program to Zip two given lists of lists. 
# Original lists:
ls1=[[1, 3], [5, 7], [9, 11]]
ls2=[[2, 4], [6, 8], [10, 12, 14]]
"""Zipped list:
	[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]"""
for v in range(len(ls1)):
    for i in range(len(ls1[v])):
        ls1[v].append(ls2[v][i])
       
print(ls1)