# Write a Python program to remove duplicates from a list of lists.      
		#Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
		#New List : [[10, 20], [30, 56, 25], [33], [40]]
lst=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
ne=[tuple(l) for l in lst]
print(ne)
new=set(ne)
new1=list(new)
print(new1)

print("by coding")
nt=[]
for i in range(len(lst)):
    if lst[i] not in nt:
        nt.append(lst[i])
print(nt) 