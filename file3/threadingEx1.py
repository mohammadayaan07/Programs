#threadingEx1.py
import threading
tname=threading.current_thread() #this id use for knowing current thread
print("default name of thread",tname.name)
dfname=threading.current_thread().name
print("default name of thread",dfname)
noat=threading.active_count() #this is use for count active thread
print("Number of active threads=",noat)