#regularexp1.py
import re
lst=[]
while(True):
	emailid=input("Enter the email Id:")
	res=re.search("\S+@\S+",emailid)
	if(res!=None):
		lst.append(emailid)
		ch=input("Do u want more mail id")
		if(ch.lower()=="no"):
			break
	else:
		print("Invalid mail ID")
print("Valid mails:{}".format(lst))