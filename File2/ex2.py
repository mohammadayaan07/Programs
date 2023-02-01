"""119. Write a Python program to check if a substring presents in a given list of string values.      
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Check if a substring presents in the said list of string values:
True
Substring to search:
abc
Check if a substring presents in the said list of string values:
False
    """
def solve(ls,val):
    for i in ls:
        set(val)
        set(i)
        if val in i:
            return True
            break
        else:
            return False
            break
    
ls=['red', 'black', 'white', 'green', 'orange']
val="abc"
print(solve(ls,val))