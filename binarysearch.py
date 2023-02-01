lst=[1,4,5,64,80,90,95]
fd=64
st=0
ed=len(lst)-1
def binary(lst,fd,st,ed):
    if st>ed:
        return -1
    mid=(st+ed)//2
    if lst[mid]==fd:
        return mid
    elif lst[mid]>fd:
        return binary(lst,fd,st,mid-1)
    else:
        return binary(lst,fd,mid+1,ed)
ab=binary(lst,fd,st,ed)
print(ab)
        