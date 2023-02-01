#febonacci.py
def feb(n):
	if n==1 or n==0:
		return 1
	feb_1=feb(n-1)
	feb_2=feb(n-2)
	return feb_1+feb_2
a=feb(6)
print(a)