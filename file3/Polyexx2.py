#polyEx2.py
class square:
	def __init__(self):
		print("Drawing Square")
class circle(square):
	def __init__(self):
		print("Drawing circle")
		square.__init__(self)
s=circle()