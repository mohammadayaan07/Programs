#choiceex2.py
import random as r
s="abcdefghijklmnopqrstuvwxyz"
S="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n="1234567890"
sp="!@#$%^&*()_+"
for i in range(1,6):
	print(r.choice(s)+r.choice(S)+r.choice(n)+r.choice(sp)+r.choice(n))