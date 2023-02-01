#Regexp1.py
import re
word=re.finditer("vr","kvrkk vk1789 234kkk")
for val in word:
	print(val.start(),val.end(),val.group())