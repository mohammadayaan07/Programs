#printingnNaturalno.py
def sum_n(n):
	if n==0:
		return 0
	s=sum_n(n-1)
	sumn=n+s
	return sumn
at=sum_n(10)
print(at)