# Write a Python program to convert a list of characters into a string. 
lst=["ayaan",123,12+09j,12.78]
re=""
for val in range(len(lst)):
    st=str(lst[val])
    print(st,type(st))