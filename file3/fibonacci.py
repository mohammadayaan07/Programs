#fibonacci.py
n=int(input("Enter the number of series you want:"))
first=0
second=1
for val in range(n):
	print(first)
	temp=first
	first=second
	second=temp+second
	print()