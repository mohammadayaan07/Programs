#Write a Python program to check whether a list contains a sublist.
lst=[1,2,3,4,5,6,7,8,9,0]
sublst=[4,50,6]
if set(sublst).issubset (set(lst)):
    print("sublst is sub lsit of list")
else:
    print("sublst is not sub set of lsit")