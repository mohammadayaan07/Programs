#regluar.py
import re
rev=re.finditer("\w+@\w+","ayann@gmail   monu@gamil.com annkdjsr")
for val in rev:
	print(val)