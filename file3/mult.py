#mult.py
import threading
def welcome():
	print("I Am from welcome()")
cs=threading.current_thread().name
print(cs)
#Program for finding default thread name
#ThreadEx1.py
from threading import *
tname=current_thread()
print("Default Name of thread=",tname.name)
		#OR
dfname=threading.current_thread().name
print("Default Name of thread=",dfname)
noat=threading.active_count()
print("Number of active threads=",noat) # 1