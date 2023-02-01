def sort(a1,a2,a):
    i,j,k=0,0,0
    while i<len(a1) and j<len(a2):
        if a1[i]>a2[j]:
            a[k]=a[i]
            k=k+1
            i=i+1
        else:
            a[k]=a2[j]
            j=j+1
            k=k+1
    while(i<len(a1)):
        a[k]=a1[i]
        i=i+1
        k=k+1
    while(j<len(a2)):
        a[k]=a2[j]
        j=j+1
        k=k+1
        
            
def soted(a):
    mid=a//2
    if len(a)==0 or len(a)==1:
        return
    a1=soted(a[0:mid])
    a2=soted(a[mid:])
    sort(1,a2,a)
a=[12,4,45,43,65,90,34,6]
ab=sorted(a)
print(ab)