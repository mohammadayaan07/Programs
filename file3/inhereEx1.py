#inhereEx1.py
class c1:
	def seta(self):
		self.a=10
class c2(c1):
	def setb(self):
		self.b=20
		self.seta()
		self.disp()
	def disp(self):
		print("val of a",self.a)
		print("val of b",self.b)
o2=c2()
o2.setb()
print("content of o2:",o2.__dict__)
