#threadingEx3.py
import threading 
def welcome():
	print("i am from the welcome()")
	print("Welcome() executed by:{}".format(threading.current_thread().name))
print("Default  thread name:{}".format(threading.current_thread().name))
t1=threading.Thread(target=welcome)
print("Default thread name",t1.name)
t1.name="KVR"
print("programmer define name for sub thread ",t1.name)
t1.start()