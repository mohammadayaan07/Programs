#Program for storing sno,sname ,marks in an object of Programmer-defined class
#StudEx2.py----Instance Data members and Class Level Data Members
class std:
	cre="Python"
s1=std()
s2=std()
print(s1.__dict__)
print(s2.__dict__)
print("Enter the element for S1\n")
s1.name=input("Enter the name")
s1.roll=int(input("Enter the roll number"))
s1.add=input("Enter the ur address")
print("*"*40)
print("\tinfo of S1")
print("*"*40)
print("name",s1.name)
print("roll",s1.roll)
print("Add",s1.add)
print("course",s1.cre)
print("course",std.cre)
print("course",s2.cre)
print("*"*40)