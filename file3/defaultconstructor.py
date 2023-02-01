#defaultconstructor.py
class student:
	def __init__(self):
		self.name="AYAAN"
		self.classs="class=x"
		self.no=10
s=student()
print(s.__dict__)
s2=student()
print(s2.__dict__)