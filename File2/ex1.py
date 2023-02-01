"""118. Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.      
Original list:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Dfference between elements (n+1th - nth) of the said list :
[1, 1, 1, 1, 1, 1, 1, 1, 1]
Original list:
[2, 4, 6, 8]
Dfference between elements (n+1th - nth) of the said list :
[2, 2, 2]"""
def solve(ls):
    l=len(ls)-1
    lst=[]
    for i in range(l):
        dif=ls[i+1]-ls[i]
        lst.append(dif)
    print(lst)

ls=[2, 4, 6, 8]
solve(ls)