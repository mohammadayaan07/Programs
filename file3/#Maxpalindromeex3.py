#Maxpalindromeex3.py
lst=[ "mom","car","madam","liril","mala","racecar"]
lspt=[(val,len(val)) for val in lst if val==val[::-1]]
print(lspt)
d=dict(lspt)
val=max(d.values())
lsms=[k for k,v in d.items() if v==val]
print(lsms)