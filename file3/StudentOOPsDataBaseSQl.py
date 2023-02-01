"""write a python program which will accept student details such as student number student name,marks in three subjects.
calculate the total marks
calculate the Percentage and give the grades.(fail/pass)

give the grade = #fail provided student secured less than 40 in any of the three subjects.
give the grade = #distinction provided student totall marks lies within 250 - 300
give the grade = #First class provided totall marks lies within 200- 249
give the grade= second class provided totall marks lies within 150- 199
give the grade= third class provided totall marks lies within 120- 149
save the students result in the database."""
#StudentOOPsDataBaseSQl.py
import mysql.connector
class student:
	def getstuddet(self):
		self.no=int(input("Enter the Student Number:"))
		self.sname=input("Enter the Student Name")
		while(True):
			self.cm=int(input("Enter the Mark of c(100):"))
			if(self.cm>=0)and(self.cm<=100):
				break
		while(True):
			self.cppm=int(input("Enter the Mark of C++ "))
			if(self.cppm>=0)and(self.cppm<=100):
				break
		while(True):
			self.pym=int(input("Enter the Mark of Python:"))
			if(self.pym>=0)and(self.pym<=100):
				break
	def compute(self):
		self.tomarks=self.cm+self.cppm+self.pym
		self.percent=(self.tomarks/300)*100
		if(self.cm<40)or (self.cppm<40)or (self.pym<40):
			self.grade="FAIL"
		else:
			if(self.tomarks>=250)and(self.tomarks<=300):
				self.grade="DISTINCTION"
			elif(self.tomarks>=200)and(self.tomarks<=249):
				self.grade="FIRST"
			elif(self.tomarks>=150)and(self.tomarks<=199):
				self.grade="SECOND"
			elif(self.tomarks>=120)and(self.tomarks<=149):
				self.garde="THIRD"
	def savestuddata(self):
		try:
			con=mysql.connector.connect(host="localhost",
			user="root",
			passwd="ERROR",
			database="batch11am")
			cur=con.cursor()
			cur.execute("insert into result values(%d,'%s',%d,%d,%d,%d,%f,'%s')"%(self.no,self.sname,self.cm,self.cppm,self.pym,self.tomarks,self.percent,self.grade))
			con.commit()
			print("student record save")
		except mysql.connector.DatabaseError as db:
			print("prob in DB",db)
s=student()
s.getstuddet()
s.compute()
s.savestuddata()



