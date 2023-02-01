#classlevelmethod.py
class student:
	@classmethod
	def getcourse(cls):
		cls.course="python"
		cls.facname()
	@classmethod
	def facname(cls):
		student.factname="kvr"
s1=student()
s2=student()
student.getcourse()
print(s1.course,s1.factname)