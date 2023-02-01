#Write a Python program to get variable unique identification number or string. 
lst=[12,34,56,"qw","ayaan"]
lst2=[12,40,34,"ayaan"]
a=[val for val in lst if val in lst2]
print(a)