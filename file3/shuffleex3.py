#program for demoinstrating shuffle()
#shuffleex3.py
import random as r
s="MISSISSIOPPI"
print("Given Data:",s)
print("Other Sufflings:")
lst=list(s)
for i in range(1,12):
	r.shuffle(lst)
	k=""
	k=k.join(lst)
	print(k)