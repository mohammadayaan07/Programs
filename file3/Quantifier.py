#Quantifier.py
import re
obj=re.finditer("[89][0-8]+","shakir89378479383902")
for val in obj:
	print(val.start(),val.end(),val.group())