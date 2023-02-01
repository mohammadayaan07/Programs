#Inhprog3.py
class Grandparent:
	def gpp(self):
		self.gpp=3.3
class parent(Grandparent):
	def pp(self):
		self.pp=float(input("enter the amount"))
class child(parent):
	def cp(self):
		self.cp=4.3
	def infop(self):
		tp=self.gpp+self.pp+self.cp
		print(self.gpp)
		print(self.pp)
		print(self.cp)
		print(tp)
s=child()
s.gpp()
s.pp()
s.cp()
s.infop()