#atmmenu.py
from Error import CaseWithdarwe,CaseDepooste,Negtive
def menu():
	print("*"*40)
	print("\tATM MENU")
	print("*"*40)
	print("\t1 CASE DEPOST")
	print("\t2 CASE WITHDRAW")
	print("\t3 BALANCE ENQIURYY")
	print("\t4 EXIT")
	print("*"*40)
bal=500.00
def balanceenquiry():
	print("YOUR CURRENT ACCOUNT BALANCE ={}".format(bal))

def casewithdarw():
	global bal
	cwith=int(input("enter the amount of withdraw mony"))
	if(cwith<0):
		raise Negtive
	elif(cwith+500>bal):
		raise CaseWithdarwe
	bal=bal-cwith
	print(" WITHDRAW MONEY= {}".format(cwith))
	print("Balance in YOUr account after withdraw ={}".format(bal))
def casedepoost():
	global bal
	dwith=int(input("enter the amount of depost"))
	if(dwith<0):
		raise CaseDepooste
	bal=bal+dwith
	print("Deposted {} is on your account.".format(dwith))
	print("Balance in your account after depost money {}".format(bal))