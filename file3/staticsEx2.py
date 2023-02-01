#staticsEx2.py
class student:
	def studentinfo(self):
		self.sname=input("enter the name of student:")
		self.sno=int(input("Enter the student no:"))
		self.subs=input("Enter the subject of student:")
		hyd.infotable(self,"teacher")
class employee:
	def employeeinfo(self):
		self.ename=input("enter the name of student:")
		self.eno=int(input("Enter the student no:"))
		self.esal=input("Enter the subject of student:")
		hyd.infotable(self,"employee")
class teacher:
	def teacherinfo(self):
		self.tname=input("enter the name of student:")
		self.tno=int(input("Enter the student no:"))
		self.tsal=input("Enter the subject of student:")
		hyd.infotable(self,"teacher")

class hyd:
	@staticmethod
	def infotable(kvr,pinfo):
		print("-"*50)
		print("Information about:{}".format(pinfo))
		for k,v in kvr.__dict__.items():
			print("\t{}   {}".format(k,v))
		print("-"*50)

s=student()
e=employee()
t=teacher()
s.studentinfo()
e.employeeinfo()
t.teacherinfo()
h=hyd()