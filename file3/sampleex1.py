#program for demoinstrating sample()
#sampleex1.py
import random as r
s="AYAANALAM"
b="1234567890"
for i in range(1,6):
	a=r.sample(s,k=3)+r.sample(b,2)
	k=""
	k=k.join(a)
	print(k)
