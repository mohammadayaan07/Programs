
"""write a python program which will accept student details such as student number student name,marks in three subjects.
calculate the total marks
calculate the Percentage and give the grades.(fail/pass)

give the grade = #fail provided student secured less than 40 in any of the three subjects.
give the grade = #distinction provided student totall marks lies within 250 - 300
give the grade = #First class provided totall marks lies within 200- 249
give the grade= second class provided totall marks lies within 150- 199
give the grade= third class provided totall marks lies within 120- 149
save the students result in the database."""
#StudentOOPsDataBaseMySQL.py
import mysql.connector
class Student:
	def  getstuddet(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		#validation of C Marks
		while(True):
			self.cm=int(input("Enter Marks in C(100):"))
			if(self.cm>=0) and (self.cm<=100):
				break
		#validation of C++ Marks
		while(True):
			self.cppm=int(input("Enter Marks in C++(100):"))
			if(self.cppm>=0) and (self.cppm<=100):
				break
		#validation of Python Marks
		while(True):
			self.pym=int(input("Enter Marks in PYTHON(100):"))
			if(self.pym>=0) and (self.pym<=100):
				break
	def compute(self):
		self.totmarks=self.cm+self.cppm+self.pym
		self.percent=(self.totmarks/300)*100
		#decide Grade
		if(self.cm<40) or (self.cppm<40) or (self.pym<40):
			self.grade="FAIL"
		else:
			if(self.totmarks>=250) and (self.totmarks<=300):
				self.grade="DISTINCTION"
			elif(self.totmarks>=200) and (self.totmarks<=249):
				self.grade="FIRST"
		
			elif(self.totmarks>=150) and (self.totmarks<=199):
				self.grade="SECOND"
			elif(self.totmarks>=120) and (self.totmarks<=149):
				self.grade="THIRD"
		
	def savestuddata(self):
		#We must write PDBC Code
		try:
			con=mysql.connector.connect(host="localhost",
			user="root",
			passwd="ERROR",
			database="batch11am")
			cur=con.cursor()
			cur.execute("insert into student values(%d,'%s',%d,%d,%d,%d,%f,'%s')" %(self.sno,self.sname,self.cm,self.cppm,self.pym,self.totmarks,self.percent,self.grade) )
			con.commit()
			print("Student Record Saved Successfully in Result Table:")
		except mysql.connector.DatabaseError as db:
			print("Prob in DB",db)
			
#main program
s=Student()
s.getstuddet()
s.compute()
s.savestuddata()
