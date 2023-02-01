#decoratorEx1.py
def square(gv):
	def getvalue1():
		n=gv()
		s=n**2
		return s
	return getvalue1
@square
def getvale():
	return int(input("Enter the value of n"))
rev=getvale()
print(rev)