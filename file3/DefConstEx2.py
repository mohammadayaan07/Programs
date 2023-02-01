#DefConstEx2.py

class const:
	def __init__(self,a=90,b=900):
		self.name=a
		self.no=b
		self.ball=400


s1=const(400,500)
print(s1.__dict__)
s1=const()
print(s1.__dict__)




class deft:
	def __init__(self):
		self.names=90
		self.clas=50
s2=deft()
print(s2.__dict__)
s3=deft()
print(s3.__dict__)