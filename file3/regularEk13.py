#reguralEx13.py
import re
obj=re.finditer("\D","KODERMA  *&%$india12345")
for val in obj:
	print(val.start(),val.end(),val.group())