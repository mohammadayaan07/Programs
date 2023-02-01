#Inhprog2.py
class C1:
	def setA(self):
		self.a=10
class C2(C1):
	def setB(self):
		self.b=20
		self.disp()
	def disp(self):
		self.setA()
		print(self.a)
		print(self.b)
s=C2()
print(s.__dict__)
s.setB()
print(s.__dict__)