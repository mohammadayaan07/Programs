def merg(a1,a2,a):
    i,j,k=0,0,0
    while(i<len(a1) and  j<len(a2) ):
        if a1[i]<a2[j]:
            a[k]=a1[i]
            k=k+1
            i=i+1
        else:
            a[k]=a2[j]
            k=k+1
            j=j+1
    while(i<len(a1)):
        a[k]=a1[i]
        k=k+1
        i=i+1
    while(j<len(a2)):
        a[k]=a2[j]
        k=k+1
        j=j+1
        
        
def mergesort(a):
    if len(a)==0 or len(a)==1:
        return 
    mid=len(a)//2
    a1=a[0:mid]
    a2=a[mid:]
    mergesort(a1)
    mergesort(a2)
    merg(a1,a2,a)
a=[1002,320,7,900,43,3]
ab=mergesort(a)
print(a)
    