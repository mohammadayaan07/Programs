#inheretenceEx2.py
class father:
	def fpop(self):
		self.fpop=float(input("enter the value of father properties:"))
		return self.fpop
class mother:
	def mpop(self):
		self.mpop=float(input("enter the value of mother properties:"))
		return self.mpop
class son(father,mother):
	def sonp(self):
		fp=self.fpop()
		mp=self.mpop()
		total=fp+mp
		print("*"*40)
		print("FATHER PROP",self.fpop)
		print("MOTHER PROP",self.mpop)
		print("SON PROP",total)
		print("*"*40)
s=son()
s.sonp()