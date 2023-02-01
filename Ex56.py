#Write a Python program to convert a string to a list. 
def change(str):
    lst=list(str.split(" "))
    return lst
str="ayaan alam koderam india"
a=change(str)
print(a)
def change1(str1):
    lst1=[]
    lst1[:0]=str1 
    return lst1
str1="ayaaan"
ab=change1(str1)
print(ab)