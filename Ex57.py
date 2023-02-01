#Write a Python program to check if all items of a given list of strings is equal to a given string. 
str="ayaan"
lst=['a','y','a','a','n']
s=""
for i in lst:
    s=s+i
if str==lst:
    print("all items of lst equal to str")   
else:
    print("all items of lst not equal to str")
print(s,type(s))



##333333333333333333333333333333333333333333333333333333

lst=["ayaan","monu","tanzil","kaif"]
name=input()
a=[i==name for i in lst]
print(a)