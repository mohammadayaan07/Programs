#UnivCollStud.py
class unvi:
	def unviput(self):
		self.uname=input("ENTER THE university name:")
		self.uloc=input("Enter the university location:")
	def uinfo(self):
		print("*"*40)
		print("\tUNIVERSITY INFO :")
		print("*"*40)
		print("\tNAME=",self.uname)
		print("\tLOCATION",self.uloc)
		print("-"*40)
class collage(unvi):
	def collagei(self):
		self.cname=input("ENTER THE university name:")
		self.cloc=input("Enter the university location:")
	def cinfo(self):
		print("*"*40)
		print("\tCOLLAGE INFO :")
		print("*"*40)
		print("\tNAME=",self.cname)
		print("\tLOCATION",self.cloc)
		print("-"*40)
class student(collage):
	def stud(self):
		self.sname=input("ENTER THE university name:")
		self.sloc=input("Enter the university location:")
		self.roll=int(input("Enter the roll of student"))
	def studinfo(self):
		print("*"*40)
		print("\tSTUDENT  INFO :")
		print("*"*40)
		print("\tNAME=",self.sname)
		print("\tLOCATION=",self.sloc)
		print("\tROLL NO=",self.roll)
		print("+"*40)

#main programe
s=student()
s.unviput()
s.uinfo()
s.collagei()
s.cinfo()
s.stud()
s.studinfo()

