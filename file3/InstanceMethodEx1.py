#Program for Reading sno,sname ,marks in an object of Programmer-defined class w.r.t Instance Methods
#InstanceMethodEx1.py
class stdu:
	cor="python"
	def readof(self):
		self.name=input("Enter ur name:")
		self.roll=int(input("Enter the roll"))
		self.addr=input("Enter the address")
	def pinfo(self):
		print("*"*50)
		print("\tname=",self.name)
		print("\troll",self.roll)
		print("\taddress=",self.addr)
		print("\tcourse",s2.cor)
		print("\tcourse",s1.cor)
		print("*"*50)

s1=stdu()
s2=stdu()
print(s1.__dict__)
print(s2.__dict__)
print("*"*50)
s1.readof()
print("*"*50)
s2.readof()
print("\tINFO OF STU 1")
s1.pinfo()
print("\tINFO OF STU 2")
s2.pinfo()
