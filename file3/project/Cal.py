import sys
print("-"*50)
print("\t1\t.Add")
print("\t2\t.Sub")
print("\t3\t.MUl")
print("\t4\t.Div")
print("\t5\t.pow")
print("\t6\t.Exit")
print("-"*50)
val=int(input("Choice Option\t[   ]\b\b\b"))
if val==6:
    sys.exit()
try:
    a=int(input("Enter One value"))
    b=int(input("Enter Second value"))
    match val:
        case 1:
            print("sum=",a+b)
        case 2:
            print("sub=",a-b)
        case 3:
            print("mul=",a*b)
        case 4:
            print("div=",a/b)
        case 5:
            print("sum=",a**b)
        case _:
            print("sorry invalid input")
except ValueError:
    print("Dont Enter The Alphabet or gaps in digit")