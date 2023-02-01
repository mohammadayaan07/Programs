#Write a Python program to find the list in a list of lists whose sum of elements is the highest. 
	#Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
	#Expected Output: [10, 11, 12]
lst=[[1,2,3], [4,5,6], [10,11,12], [7,8,90]]
max=sum(lst[0])
for i in range(len(lst)):
    if max<sum(lst[i]):
        max=sum(lst[i])
        l=i
print(lst[l])