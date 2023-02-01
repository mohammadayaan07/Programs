#Write a Python program to move all zero digits to end of a given list of numbers. 
	#Expected output:
	#Original list:
lst=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
	#Move all zero digits to end of the said list of numbers:
	#[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(lst)):
    if lst[i]==0:
        lst+=[lst.pop(lst[i])]
print(lst)
         