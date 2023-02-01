#Write a Python program to convert a list of multiple integers into a single integer. 
#		Sample list: [11, 33, 50]
#		Expected Output: 113350
lst=[12,34,56]
sm=""
for i in range(len(lst)):
    sm=sm+str(lst[i])
print(sm)