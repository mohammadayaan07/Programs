#atmfinal.py
from ERROR1 import*
bal=500
def withdraw():
	global bal
	val=float(input("enter the amount of withdar"))
	if val<0:
		raise NoBalError
	elif val+500>bal:
		raise NoMonyError
	bal=bal-val
	print("Total amount withdraw from your account {}".format(val))
	print("Total amount after withdraw amount from your account {}".format(bal))
def deposit():
	global bal
	dep=float(input("Enter the amount of deposit"))
	if dep<0:
		raise NoBalError
	bal=dep+bal
	print("Total amount deposit from your account {}".format(dep))
	print("Total amount after deposit amount from your account {}".format(bal))
def balqury():
	print("total bal in your account={}".format(bal))

