#inheretenEx2.py
try:
	class grandparent:
		def gppop(self):		
			self.gppop=float(input("Enter the property of GP"))
	class parent(grandparent):
		def ppop(self):
			self.ppop=float(input("Enter the property of FP"))
	class son(parent):
		def spop(self):
			self.spop=float(input("Enter the property of SP"))
		def totalpop(self):
			self.ppop()
			self.gppop()
			self.spop()
			total=self.spop+self.ppop+self.gppop
			print("*"*40)
			print("\tGrandparent prop=",self.gppop)
			print("\tParent prop=",self.ppop)
			print("\tSon prop=",self.spop)
			print("*"*40)
			print("\tTotal prop=",total)
			print("*"*40)
except ValueError:
	print("Dont enter the str of alpha numric in properties")


s=son()
s.totalpop()

