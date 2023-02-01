def  kvrrange(b,e,s):
	while(b<=e):
		yield b
		b=b+s

#main program
k=kvrrange(10,50,5) # here k is an object <class, generator>
print(next(k))
