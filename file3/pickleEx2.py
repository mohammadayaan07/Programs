#pickleEx2.py
import pickle
with open("std.data","rb") as fp:
	print("\tname \trollno")
	try:
		while(True):
			obj=pickle.load(fp)
			for val in obj: 
				print("\t{}".format(val) ,end="")
			print()
	except EOFError:
		print("\tits over")