#userno.py
import re
mno=input("enter the phone number:")
if(len(mno)==10):
	res=re.search("[6789][\d{9}]",mno)
	if(res!=None):
		print("valid phone number")
	else:
		print("Dont enter the str or alphanumbric")
else:
	print("Invalid phone number")