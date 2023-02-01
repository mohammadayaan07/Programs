# Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
#Sample list: [0,1,2,3,4,5]
#Expected Output: [1, 0, 3, 2, 5, 4]
lst=[1,2,3,4,5]
for i in range(len(lst)):
    lst[i]=lst[i+1]