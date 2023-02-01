#Write a Python program to generate all sublists of a list. 
lst=[1,2,3,4]
lt=[[]]
for i in range(len(lst)):
    for v in range(i):
        lt.append(lst[v:i])
print(lt)