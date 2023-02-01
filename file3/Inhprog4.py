#Inhprog3.py
class father:
	def father(self):
		self.fp=12.90
class mother:
	def mother(self):
		self.mp=11.0
class child(father,mother):
	def infor(self):
		self.mother()
		self.father()
		tot=self.mp+self.fp
		print(self.mp)
		print(self.fp)
		print(tot)
s=child()
s.infor()