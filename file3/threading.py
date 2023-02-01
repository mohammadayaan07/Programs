#threading.py
import time,threading
def square(lst):
	for val in lst:
		sq=val**2
		print("Sub",threading.current_thread().name)
		print(sq)
		time.sleep(1)

def cube(lst):
	for val in lst:
		cb=val**3
		print("Sub",threading.current_thread().name)
		print(cb)
		time.sleep(1)



bt=time.time()
print("name=",threading.current_thread().name)
lst=[1,2,3,4,7,8]
square(lst)
cube(lst)
et=time.time()
print("Total time=",et-bt)