def lst1():
    lst=[]
    n=int(input("enter the number to insert in lst:"))
    for val in range(n):
        lst2=int(input("enter the lst values"))
        lst.append(lst2)
    return lst

lat1=lst1()
print(lat1)
set1=set(lat1)
def check():
    if len(set1)==len(lat1):
        print("True")
    else:
        print("False") 
check()