#ployEx3.py
class Square:
	def __init__(self):
		print("drawing square")
class rect(Square):
	def __init__(self):
		print("drawing rectange")
		Square.__init__(self)
s=rect()
