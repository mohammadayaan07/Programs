#threadingEx2.py
import threading
def welcome():
	print("\ni am from welcome()")
	print("welcome() execute by :{}".format(threading.current_thread().name))
print("Default thread name: {}".format(threading.current_thread().name))
t1=threading.Thread(target=welcome)
es=t1.is_alive()#for checking sub thread is under start or not
print("is sub thread under execution befor start() {}".format(es))
t1.start() #start the sub thread
print("is sub thread under execution befor start() {}".format(t1.is_alive()))