#Write a Python program to check whether all dictionaries in a list are empty or not. 
"""Sample list : [{},{},{}]
	Return value : True
	Sample list : [{1,2},{},{}]
	Return value : False"""
def check(smpl):
    l=True
    for i in range(len(smpl)):
        if len(smpl[i])>0:
            return False 
    return l
smpl=[{},{},{},{10}]
a=check(smpl)
print(a)
