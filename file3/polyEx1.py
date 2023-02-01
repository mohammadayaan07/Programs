#polyEx1.py
class ract:
	def draw(self):
		print("Drawing rect")
class circle(ract):
	def draw(self):
		print("drawing circle")
class square(circle):
	def draw(self):
		print("drawing square")
		ract.draw(self)
		circle.draw(self)
s=square()
s.draw()