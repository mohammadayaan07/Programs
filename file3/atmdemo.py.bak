#atmdemo.py
from atmmenu import menu,balanceenquiry,casewithdarw,casedepoost
import sys
from Error import CaseDepooste,CaseWithdarwe,Negtive
while(True):
	menu()
	try:
		ch=int(input("enter the option:"))
		match(ch):
			case 1: 
				try:
					casedepoost()
				except CaseDepooste:
					print("dont enter negative amount")
				except ValueError:
					print("DONT enter speical char")
			case 2:
				try:
					casewithdarw()
				except Negtive:
					print("Dont enter negative amonut")
				except CaseWithdarwe:
					print("YOU dont have sufficient ammount")
				sys.exit()
			case 3:
				balanceenquiry()
			case 4:
				print("THANKS YOU FOR USING ATM")
				sys.exit()
			case _:
				print("Dont enter invalid option")
	except ValueError:
		print("DONT ENTER STR OR SPCIAL CHAR")