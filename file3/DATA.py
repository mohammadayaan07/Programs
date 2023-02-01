#DATA.py
import re
s="Rossum got 22 marks , Dennis got 11 marks , Travis got 44 marks , Kinney got 55  marks and James got 999 marks and Guru got 55 marks and Kvr got 11 marks"
fp="\d{2,3}"
fd=re.findall(fp,s)
for val in fd:
	print(val)