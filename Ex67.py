def check(lst,n):
    if len(lst)==0:
        return -1
    if lst[0]==n:
        return 0
    smalloutput=lst[1:]
    out=check(smalloutput,n)
    return out+1
lst=[12,3,45,34,34212,2,3,1]
x=1
ab=check(lst,x)
print(ab)