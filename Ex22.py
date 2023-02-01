#Write a Python program to find the index of an item in a specified list. 
lst=[12,"1672","ayaan",14]
fd=input("enter thing u want")
def fnd(lst,fd):
    for index,val in enumerate(lst):
        if str(val)==fd:
            print(index)
            break
        else:
            print("not found")
            break
        
fnd(lst,fd)

    