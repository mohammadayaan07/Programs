#regularEk11.py
import re
obj=re.finditer("\D","Koderma #4985*& INDIA")
for val in obj:
	print("Start={} end={} and value={}".format(val.start(),val.end(),val.group()))