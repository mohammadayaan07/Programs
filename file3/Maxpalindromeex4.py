#Maxpalindromeex4.py
lst=[ 1, 232, 5545455, 999999, 1212 , 8558 ]
lmc=[(str(val),len(str(val))) for val in lst if str(val)==str(val)[::-1]]
print(lmc)
d=dict(lmc)
val=max(d.values())
print(val)
maxpalin=[ k for k,v in d.items() if v==val]
print(maxpalin[-1])