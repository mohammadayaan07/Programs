def lastindex(lst,n,si):
    l=len(lst)
    if si==l:
        return -1
    output=lastindex(lst,n,si+1)
    if output!=-1:
        return output
    else:
        if lst[si]==n:
            return si
        else: 
            return -1
lst=[1,2,3,4,56,7,4]
n=4
si=0
print(lastindex(lst,n,si))