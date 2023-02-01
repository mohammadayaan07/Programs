#inheritance.py
class c1:
	def grandfather(self):
		self.a=1000
class c2(c1):
	def father(self):
		self.b=1200
class c3(c2):
	def child(self):
		self.c=1220
	def pinfo(self):
		self.ac=self.father()
		self.dc=self.grandfather()
		self.bc=self.child()
		print(self.a)
		print(self.b)
		print(self.c)
		s=self.a+self.c+self.b
		print(s)
s=c3()
s.pinfo()