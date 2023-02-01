#reguralEx13.py
import re
obj1=re.finditer(".","KvKVkVKKVKQvKKK")
for val in obj1:
	print(val.start(),val.end(),val.group())
print("+++++++++")
obj=re.finditer("K*","KKKKVRKGKHKJKKSHHIWKKKHKK")
for val in obj:
	print(val.start(),val.end(),val.group())
print("_____")
obj2=re.finditer("K?","KHWKKKKEBWHJDKHKK")
for val in obj2:
	print(val.start(),val.end(),val.group())

	#quantifier are use in 4 ways
	#k-- it mean number of all k
	#k+-- it mean sequance of kk kkkk come
	#k?-- only single k and other space
	#k*--- squance of kkk other space
	#. -- all thing it will print

