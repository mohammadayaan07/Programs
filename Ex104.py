""" Write a Python program to find the difference between consecutive numbers in a given list. 
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]
Difference between consecutive numbers of the said list:
[0, 2, 1, 0, 1, 1, 1]
Original list:
[4, 5, 8, 9, 6, 10]
Difference between consecutive numbers of the said list:
[1, 3, 1, -3, 4]
"""
def con(lst):
    ls=[]
    for i in  range(len(lst)-1):
        s=lst[i+1]-lst[i]
        ls.append(s)
    return ls
lst=[4, 5, 8, 9, 6, 10]
ab=con(lst)
print(ab)
        