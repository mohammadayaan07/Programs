#inheritence.py
class s1:
	def __init__(self):
		self.a=100
class s2(s1):
	def __init__(self):
		self.b=200
	def pinfo(self):
		print(self.a)
		print(self.b)

W=s2()
W.pinfo()