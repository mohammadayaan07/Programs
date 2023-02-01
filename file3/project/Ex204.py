"""Write a Python program to check if first digit/character of each element in a given list is same or not.      
Original list:
[1234, 122, 1984, 19372, 100]
Check if first digit in each element of the said given list is same or not!
True"""
ls=[1234, 122, 1984, 19372, 2100  ]
def check(ls):
    lst=[]
    for i in ls:
        val=str(i)
        print(val)
        lst.append(val[0])
    if len(set(lst))==1:
        return True
    else:
        return False
    
print(check(ls))
        