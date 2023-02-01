#atmdemo1.py
from atm1 import atm
from atmfinal import*
from ERROR1 import NoMonyError,NoBalError
import sys
atm()
while(True):
	try:
		ch=int(input("enter your option:"))
		match(ch):
			case 1:
				try:
					withdraw()
				except NoMonyError:
					print("You dont have sufficient Mount to withdraw")
				except NoBalError:
					print("Dont enter negative amount of withdraw")
				except ValueError:
					print("no str")
			case 2:
				try:
					deposit()
				except NoBalError:
					print("Dont enter negative amount of withdraw")
				except ValueError:
					print("NO symbol")
			case 3:
				balqury()
			case 4:
				print("THANK YOU FOR USING ATM")
				sys.exit()
			case _:
				print("DONT ENTER THE INVALID OPTION")
	except ValueError:
		print("DONT ENTER THE SPEICAL CHAR OR SYMBOLS")
	




