#pickleEx1.py
import pickle,sys
with open("std.data","ab") as fp:
	while(True):
		l1=list()
		rool=int(input("enter the roll"))
		name=input("ENter the name")
		l1.append(name)
		l1.append(rool)
		pickle.dump(l1,fp)
		ch=input("do you want more info yes or no")
		if ch.lower()=="no":
			sys.exit()