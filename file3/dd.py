#dd.py
import re
obj=re.finditer("[\dd]","!@#jhk112312")
for val in obj:
	print(val.start(),val.end(),val.group())