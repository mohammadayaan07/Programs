#classlevelmethodex4.py
class student:
	@classmethod
	def sub(cls):
		cls.sub="Pyhton"
		cls.fact="kvr"
		cls.batchtime()
	@classmethod
	def batchtime(cls):
		student.batchtime="11.am"
	def studentid1(self,sname,rollno,smarks):
		self.sname=sname
		self.rollno=rollno
		self.smarks=smarks

	def studentid(self):
		self.sub()
		print("*"*40)
		print(self.sname)
		print(self.rollno)
		print(self.smarks)
		print(self.fact)
		print(self.sub)
		print(self.batchtime)
		print("*"*40)
s1=student()
s1.studentid1("AYAN",10,100)
s1.studentid()