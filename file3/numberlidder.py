#numberlidder.py
n=int(input("Enter the no of Row"))
num=1
for i in range(1,n+1):
	for v in range(1,i+1):
		print(num,end="")
		num=num+1
	print()
	

