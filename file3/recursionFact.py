#recursionFact.py
import math
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)
n=int(input("Enter the values of N:"))
result=fact(n)
print("Fact of {} = {}".format(n,result))

