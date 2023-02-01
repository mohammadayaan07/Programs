#new.py
def lastfind(a,x,si):
    l=len(a)
    if a==0 or a==x:
        return -1
    smlst=lastfind(a,x,si+1)
    if smlst!=-1:
        return smlst
    else:
        if a[si]==x:
            return si
        else:
            return -1
        
a=[1,2,3,456,4,66,64,4,90]
x=4
si=0
prt=lastfind(a,x,si)
print(prt)