"""Write a Python program to find the indexes of all None items in a given list.      
Original list:
[1, None, 5, 4, None, 0, None, None]
Indexes of all None items of the list:
[1, 4, 6, 7]"""
def check(lst):
    ls=[]
    for i in range(len(lst)):
        if lst[i]==None:
            ls.append(i)
    return ls
lst =[1, None, 5, 4, None, 0, None, None]
print(check(lst))
