#DestEx3.py
import time
class Student:
	def __init__(self,sno,sname):
		print("I am from PC")
		self.sno=sno
		self.sname=sname
		print("\t{}\t{}".format(self.sno,self.sname))
	
	def  __del__(self):
		print("GC calls __del__")

#main program
print("\nProgram Execution Started")
s1=Student(10,"RS")# Object Creation
s2=s1 # Object Creation
s3=s1
print("Now we are No Longer interested in maintaing S1 object memory space:")
s1=None # Calling GC Forcefully and it inturns calls Destructor
print("Now we are No Longer interested in maintaing S1 object memory space:")
del s2 # Calling GC Forcefully and it inturns calls Destructor
print("Now we are No Longer interested in maintaing S1 object memory space:")
del s3 # Calling GC Forcefully and it inturns calls Destructor


