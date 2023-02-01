#destEx1.py
import sys,gc
class student:
	def __init__(self,sno,sname):
		print("i am from pc")
		self.sno=sno
		self.sname=sname
		print("\t{}\t{}".format(self.sno,self.sname))
	def __del__(self):
		print("gc call __del__")
s1=student(10,"rs")
s2=student(200,"lt")
s3=student(20,"kv")
totmem=sys.getsizeof(s1)+sys.getsizeof(s2)
print(totmem)
print("end")
s1=None #first method
gc.disable()
del s2  #second method
print(totmem)

