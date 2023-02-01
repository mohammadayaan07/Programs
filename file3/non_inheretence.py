#WiththreadingEx1.py
import threading,time
def findsquares(lst):
	for val in lst:
		print("5-->Therad Name:{}-->Square({})={}".format(threading.current_thread().name,val,val**2))
		time.sleep(1)

def findcubes(lst):
	for val in lst:
		print("10-->Therad Name:{}-->cubes({})={}".format(threading.current_thread().name,val,val**3))
		time.sleep(1)

#main program
bt=time.time()
print("Line-15->Default Name Thread in main program=",threading.current_thread().name) # Main Thread
print("Initial Number of Threads=",threading.active_count())
lst=[12,5,6,10,23,-5,15]
#create sub threads/ child threads
t1=threading.Thread(target=findsquares,args=(lst,) ) # Thread-1
t2=threading.Thread(target=findcubes,args=(lst,))# Thread-2
t1.name="ROssum"
t2.name="Travis"
t1.start()
t2.start()
print("Number of Threads=",threading.active_count())
t1.join()
t2.join()
print("Number of Threads=",threading.active_count())
et=time.time()
print("Total Time Taken by Threads Program={}".format(et-bt))