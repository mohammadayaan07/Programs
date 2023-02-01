# Write a Python program to find the items starts with specific character from a given list. 
"""Expected Output:
		Original list:
		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
		Items start with a from the said list:
		['abcd', 'abc', 'acjd']
		Items start with d from the said list:
		['dagfa']
		Items start with w from the said list:
		[]"""
lst=['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
def fd(lst,w):
    c=0
    for i in range(len(lst)):
         if w==lst[i][0]:
            print(lst[i])
            c=c+1
    if c==0:
        print("[]")
            
        
fd(lst,"m")