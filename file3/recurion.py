#recurion.py
def sortlst(lst,ind):
	l=len(lst)
	if ind==l-1 and ind==l:
		return True
	if lst[ind] > lst[ind+1]:
		return False
	
	output=sortlst(lst,ind+1)
	return output
a=[1,2,3,4,5]
ind=0
b=sortlst(a,ind)
print(b)