#inheritance.py
class c1:
	def info1(self):
		self.a=100
class c2(c1):
	def info2(self):
		self.b=120
	def pinfo(self):
		print(self.a)
		print(self.b)
s=c2()
s.info1()
s.info2()
s.pinfo()