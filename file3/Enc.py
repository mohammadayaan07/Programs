#encapsulationAbstraction.py
class info:
	def __infostd(self):
		self.name="Ayaan"
		self.course="python"
		self.__age="21"
		self.no=1234
	def prt(self):
		print("Name=",self.name)
		print("course=",self.course)
		#print("age=",self.age)
		print("no",self.no)
s=info()
s.infostd()
s.prt()