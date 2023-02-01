#Write a Python program that removes vowels from a string.?
str=input("enter the str:")
lst1=list(str)
vowel=["a","e","i","o","u"]
lst=[]
re = ""
for val in str:
    if val.lower() in vowel:
        continue
    else:
        lst.append(val)
print(lst)
newstr=re.join(lst)
print(newstr)
val=[i for i in lst1 if i not in vowel]


new=re.join(val)
print(new)