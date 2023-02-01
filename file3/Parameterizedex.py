#Parameterizedex1.py
class student:
	def __init__(self,a,b):
		self.name=a
		self.roll=b
		print("ur name is {}".format(self.name))
		print("UR ROLL NO IS {}".format(self.roll))
s=student(input("enter a name"),int(input("ENTER YOUR ROLL NO")))
	