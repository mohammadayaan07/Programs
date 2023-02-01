#sortedoflst.py
def sortlst(a):
	l=len(a)
	if l==0 and l==1:
		return True
	if a[0]>a[1]:
		return False
	smallestlst=a[1:]
	issort=sortlst(smallestlst)
	if issort:
		return True
	else:
		return False
b=[1,2,3,4]
str=sortlst(b)
print(str)