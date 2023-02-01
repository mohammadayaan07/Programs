#Write a Python program to print the numbers of a specified list after removing even numbers from it. 

lst=[1,2,3,4,5,6,100,105]
newlst=[val for val in lst if val%2!=0]
print(newlst)