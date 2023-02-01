#recursionsum.py
def sumn(n):
	if n==0:
		return 0
	return n+sumn(n-1)
s=sumn(10)
print(s)