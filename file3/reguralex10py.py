#reguralex10py
import re
mp=re.finditer("[^a-zA-Z0-9]","kOdermaWORLD  *#123india")
for val in mp:
	print(val.start(),val.end(),val.group())