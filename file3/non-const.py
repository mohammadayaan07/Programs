#non-const.py
class student:
	def __init__(self,a,b):
		self.name=input("Enter the name of student:")
		self.classs=input("Enter the classs of student:")
		self.no=int(input("Enter the student no:"))
		print("*"*40)
		print("NAme=",self.name)
		print("class",self.classs)
		self.a=a
		self.b=b
		print("no",self.no)
		print("a=",self.a)
		print("b=",self.b)
		print("*"*40)
s=student(100,200)
s2=student("koderma",2090)