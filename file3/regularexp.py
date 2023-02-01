#regularexp.py
import re
S="Rossum maild is rossum123@psf.com , Dennis maild is dennis_c@bellland.co.in  , Travis maild is travis_numpy@numpy.org , Kinney  maild is kinney_pandas@pandas.net.in and James maild is james.java@sun.com and Kvr mail is Kvr1.Java@gmail.com"
fd="\S+@\S+"
finda=re.findall(fd,S)
for val in finda:
	print(val)
name=re.finditer("[A-Z]+")
print(name)