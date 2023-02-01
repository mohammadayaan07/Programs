#classesEx1.py
class snamek:
	plc="koderma"
	are="jalwabad koderma india"



s1=snamek()
s2=snamek()
print("obj before implement {}".format(s1.__dict__))
print("obj before implement {}".format(s2.__dict__))
print("*"*50)
s1.sanme="hadi"
s2.samne="Ahad"
s1.age=4
s2.age=3
print("\tELEMENT OF S1 OBJECT")
print(s1.__dict__)
print("*"*50)
print(s1.sanme)
print(s1.age)
print(s1.plc)
print(snamek.are)
print("*"*50)


print("\tElement of s2 obj")
print(s2.__dict__)
print(s2.samne)
print(s2.age)
print(snamek.plc)
print(s2.are)