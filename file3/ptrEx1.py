#ptrEx1.py
def fib(n):
	if n==1 or n==2:
		return 1
	s_1=fib(n-1)
	s_2=fib(n-2)
	output=s_1+s_2
	return output
a=fib(4)
print(a)