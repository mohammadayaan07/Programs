def firstindex(lst,n):
    l=len(lst)
    if l==0:
        return -1
    if l==1:
        return 0
    if lst[0]==n:
        return 1
    small=lst[1:]
    output=firstindex(small,n)
    return output +1
lst=[1,34,2,3]
n=3
a=firstindex(lst,n)
print(a)

def firstindex1(lst,n,si):
    l=len(lst)
    if l==0:
        return -1
    if si==l or si==l-1:
        return si
    if lst[si]==n:
        return si
    output=firstindex1(lst,n,si+1)
    return output
lst=[1,34,23,56,454,2,3]
n=3
si=0
a=firstindex1(lst,n,si)
print(a)