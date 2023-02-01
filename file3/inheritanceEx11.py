#instancesEx2.py
class student:
	def studinfo(self):
		print("*"*40)
		self.name=input("Enter the name of student:")
		self.classs=input("Enter the course of student:")
		self.sub=input("enter the sub of student")
		print("*"*40)
		self.desinfo()
	def desinfo(self):
		print("NAME=",self.name)
		print("class=",self.classs)
		print("sub=",self.sub)

s1=student()
s2=student()
print(s1.__dict__)
s1.studinfo()
s2.studinfo()

