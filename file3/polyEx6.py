#polyEx6.py
class Square:
	def area(self):
		self.a=int(input("Enter the Side"))
		self.area=self.a**2
		print("Area of Square:",self.area)
		print("*"*40)
class rect:
	def __init__(self):
		self.l=int(input("Enter the length"))
		self.b=int(input("Enter the breath"))
		self.area=self.l*self.b
		print("*"*40)
		print("Area of Rect:",self.area)
class circle(rect,Square):
	def __init__(self,r):
		self.r=r
		self.area=3.14*self.r**2
		print("Area of Circle:",self.area)
		print("*"*40)
		super().__init__()
		Square.area(self)
r=int(input("Enter the radius"))
s=circle(r)
