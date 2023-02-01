#Program for Reading sno,sname ,marks in an object of Programmer-defined class w.r.t Instance Methods
#InstanceMethodEx2.py
class stdu:
	crs="Python"
	def infor(self):
		self.name=input("Enter the name:")
		self.No=int(input("Enter the id No:"))
		self.addr=input("Enter the address:")
		self.infop()
	def infop(self):
		print("*"*50)
		print("\tName:",self.name)
		print("\tID NO:",self.No)
		print("\tAddress:",self.addr)
		print("\tCOURSE=",stdu.crs)
		print("*"*50)
#main program
s1=stdu()
s2=stdu()
print("Element in ",s1.__dict__)
s1.infor()
s2.infor()