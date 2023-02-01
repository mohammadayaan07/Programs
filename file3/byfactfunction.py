#byfactfunction.py
def fact(n):
	rs=1
	for val in range(1,n+1):
		rs=rs*val
	return rs
n=int(input("Enter the values of N:"))
rs=fact(n)
print("Fact of {} = {}".format(n,rs))

