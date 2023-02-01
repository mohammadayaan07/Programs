#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
#		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#		Expected Output : ['Green', 'White', 'Black']
SampleList=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
NSampleList=SampleList[1::2]
print(NSampleList)


SampleList=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
chk=['Red','White',  'Pink']
lst=[val for val in SampleList if val not in chk]
print(lst)