#ployEx9.py
class Rect:
	def __init__(self):
		self.l=int(input("l="))
		self.b=int(input("b="))
		area=self.l*self.b
		print("AREA OF RECT:",area)
class Square(Rect):
	def __init__(self):
		self.a=int(input("a="))
		area=self.a**2
		print("AREA OF Square:",area)
class circle(Square):
	def __init__(self):
		self.r=float(input("r="))
		area=3.14*self.r**2
		print("AREA OF CIRCLE:",area)
		super().__init__()
		Rect.__init__(self)
s=circle()


