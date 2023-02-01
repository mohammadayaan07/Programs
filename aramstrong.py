#aramstrong
num=int(input("enter the number:"))
temp = num
cube=0
while(num!=0):
    a=num%10
    num=num//10
    cube = cube+a**3
if cube==temp:
    print("is")
else:
    print("is not")