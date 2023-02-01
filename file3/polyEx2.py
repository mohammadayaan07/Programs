#polyEx2.py
class circle:
	def draw(self):
		print("drawing circle")
class square(circle):
	def draw(self):
		print("drawing square")
class rect(square):
	def draw(self):
		print("drawing rect")
		super().draw()
		circle.draw(self)
s=rect()
s.draw()