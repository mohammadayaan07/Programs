#StaticMethodEx2.py
class student: 
	def student(self):
		self.NAME=input("ENTER THE STUDENT NAME:")
		self.CLASS=int(input("ENTER THE CLASS"))
		self.ROLLNO=int(input("ENTER THE ROLLNO :"))
		kvr.desp(self,"STUDENT")
		
class employee:
	def employee(self):
		self.NAME=input("ENTER THE EMPLOYEE NAME:")
		self.SALARY=int(input("ENTER THE SALARY OF EMPLOYEE"))
		self.NO=int(input("ENTER THE Number :"))
		kvr.desp(self,"EMPLOYEE")
class teacher:
	def teacher(self):
		self.NAME=input("ENTER THE TEACHER  NAME:")
		self.CLASS=int(input("ENTER THE CLASS"))
		self.INCOME=int(input("ENTER THE INCOME :"))
		kvr.desp(self,"TEACHER")
		
class kvr:
	@staticmethod
	def desp(self,name):
		print("*"*50)
		print("\tINFO OF \t{}".format(name))
		for key,val in self.__dict__.items():
			print("\t{}=\t\t{}".format(key,val))
		print("\tINSTITUE NAME={}".format(clsmethod.crs))
		print("*"*50)
class clsmethod:
	@classmethod
	def schools(cls):
		cls.crs="nit"

m=clsmethod()
m.schools()
s=student()
s.student()
e=employee()
e.employee()
t=teacher()
t.teacher()
d=kvr()


