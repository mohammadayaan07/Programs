#shuffle.py
import random as r
s="AyaanALAM"
lst=list(s)
for i in range(1,6):
	r.shuffle(lst)
	k=""
	k=k.join(lst)
	print(k)