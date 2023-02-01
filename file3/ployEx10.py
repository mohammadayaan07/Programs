#ployex10.py
class Square:
	def __init__(self,a):
		area=a**2
		print("AREA OF Square",area)
class Rect:
	def __init__(self,l,b):
		area=l*b
		print("AREA OF RECT",area)
class Circle(Rect,Square):
	def __init__(self,r):
		self.area=3.14*r**2
		print("AREA OF CIRCLE:",self.area)
		print("*"*50)
		super().__init__(int(input("Enter the breath")),int(input("Enter the length")))
		print("*"*50)
		Square.__init__(self,int(input("Enter the length")))
r=float(input("ENTER THE RADIUS"))
s=Circle(r)