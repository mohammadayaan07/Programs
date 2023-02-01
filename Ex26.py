#Write a python program to check whether two lists are circularly identical.
lst=[12,13,4,56]
lst1=[4,13,12,56,90]
lst2=[]
l1= len(lst)
l2= len(lst1)
if l1!=l2:
    print("Both have differnt elment")
else:
    for i in range(l1):
        for v in range(l2):
            if lst[i] == lst1[v]:
                lst2.append(lst[i])
    if lst==lst2:
        print("same")
    else:
        print("not same")
        