#studopspickle.py
from Student import student
import pickle,sys
class studinforead:
	def studinfo(self):
		with open("student.data","ab")as fp:
			while(True):
				sname=input("Enter the name")
				sno=int(input("Enter the no"))
				marks=int(input("enter the marks"))
				s=student(sno,sname,marks)
				pickle.dump(s,fp)
				print("Student data is save")
				print("*"*50)
				ch=input("u want to inserct more record yes /no")
				if(ch.lower()=="no"):
					print("THANKS FOR USING DATA")
					print("*"*50)
					sys.exit()
		
sp=studinforead()
sp.studinfo()