#polEx1.py
class Circle:
	def draw(self):
		print("drawing circle")
class Rect(Circle):
	def draw(self):
		print("drawing rect")
		super().draw()
class square(Rect):
	def draw(self):
		print("drawing square")
		super().draw()
s=square()
s.draw()