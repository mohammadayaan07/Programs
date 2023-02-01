#DestEx7.py
import time
class Student:
	def __init__(self,sno,sname):
		print("I am from PC")
		self.sno=sno
		self.sname=sname
		#print("\t{}\t{}".format(self.sno,self.sname))
	
	def  __del__(self):
		print("GC calls __del__")

#main program
print("\nProgram Execution Started")
s1=Student(10,"RS")# Object Creation
s2=s1 #Deep Copy
s3=s1 #Deep Copy
print("Now we are No Longer interested in maintaing S1 object memory space:")
time.sleep(5)
s1=None   # GC will not call __del__(self) bcoz still s2 and s3 to same memory space
print("Now we are No Longer interested in maintaing S2 object memory space:")
time.sleep(5)
del s2   # GC will not call __del__(self) bcoz still s3 to same memory space
print("Now we are No Longer interested in maintaing S3 object memory space:")
time.sleep(5)
del s3   # GC will not call __del__(self) bcoz still s3 to same memory space
print("\nProgram Execution Ended")
time.sleep(5)
s4=Student(100,"koderma")
#Here GC will not call   __del__(self) 