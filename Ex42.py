#Write a Python program to find missing and additional values in two lists.      
#	Sample data : Missing values in second list: b,a,c
#	Additional values in second list: g,h
lst=['a','b','c','d','e','f']
ab=['d','e','f','g','h']
print("Miss",set(ab).difference(lst))
print("additional",set(lst).difference(ab))