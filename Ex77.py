#Write a Python program to decode a run-length encoded given list.
"""	Original encoded list:
	[[2, 1], 2, 3, [2, 4], 5, 1]
	Decode a run-length encoded said list:
	[1, 1, 2, 3, 4, 4, 5, 1]"""
a=[[2, 1], 2, 3, [2, 4], 5, 1]
ab=[]
for i in a:
    if type(i) is list:
        for v in i :
            ab.append(v)
    else:
        ab.append(i)
print(ab)