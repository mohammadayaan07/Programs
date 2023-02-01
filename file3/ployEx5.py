#ployEx5.py
class Rect:
	def area(self):
		self.l=int(input("l="))
		self.b=int(input("b="))
		area=self.l*self.b
		print("AREA OF RECT:",area)
class Square(Rect):
	def area(self):
		self.a=int(input("a="))
		area=self.a**2
		print("AREA OF Square:",area)
		super().area()
class circle(Square):
	def area(self):
		self.r=float(input("r="))
		area=3.14*self.r**2
		print("AREA OF CIRCLE:",area)
		super().area()

s=circle()
s.area()


