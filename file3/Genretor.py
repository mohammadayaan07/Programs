#Genretor.py
def kvrrange(b,v,s):
	while(b<=v):
		yield b
		b=b+s
k=kvrrange(10,15,2)
while(True):
	try:
		print(next(k))
	except StopIteration:
		break