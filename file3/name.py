nm=input("Enter the Name")
n=len(nm)
for val in range(0,n+1):
	for val2 in range(0,val+1):
		print(nm[val2],end="")
	print()