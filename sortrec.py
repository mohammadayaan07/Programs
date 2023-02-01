def swap():
    lst=[10,30,20,6,5]
    print(lst)
    temp = 0
    for i in range(0,len(lst)-1):
        for j in range(len(lst)-1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst
new = swap()
print(new)