#febonaci.py
def feb_n(n):
	if n==1 or n==2:
		return 1
	feb_n_1=feb_n(n-1)
	feb_n_2=feb_n(n-2)
	output=feb_n_1+feb_n_2
	return output
s=feb_n(5)
print(s)