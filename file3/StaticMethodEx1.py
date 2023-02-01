#StaticMethodEx1.py
class student:
	def stu(self):
		self.studentname=input("Enter the student Name:")
		self.roll=int(input("enter the roll"))
class employee:
	def emp(self):
		self.employeename=input("Enter the employees Name:")
		self.income=int(input("enter the INcome:"))
class teacher:
	def tec(self):
		self.teachername=input("Enter the Teacher Name:")
		self.salary=int(input("enter the Salary"))
class hyd:
	@staticmethod
	def disp(kvr,m):
		print("\t{} INFO".format(m))
		print("*"*40)
		for i,v in kvr.__dict__.items():
			print("{}-----{}".format(i,v))

s=student()
e=employee()
t=teacher()
s.stu()
e.emp()
t.tec()
hyd.disp(s,"STUDENT ")
hyd.disp(e,"EMPLOYEES")
hyd.disp(t,"TEACHER")