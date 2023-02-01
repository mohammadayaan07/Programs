lst=["ayaan","monu","tanzil","kaif"]
name1=input("enter the name :")
for i in lst:
    if name1==i:
        print("found")
    elif name1 not in lst:
        print("not found")
        break
        
        