#Write a python program which will generate 1 to n numbers after each and every second
#NumbergenEx1.py
import time,threading
def numbergenerate(n):
	print("Name of the thread in number:{}".format(threading.current_thread().name))
	if(n<=0):
		print("Invalid input {}".format(n))
	else:
		print("*"*40)
		print("numbwer within :{}".format(n))
		print("*"*40)
		for i in range(1,n+1):
			print("\t{}".format(i))
			time.sleep(1)
		print("*"*40)
n=int(input("Enter the number"))
t1=threading.Thread(target=numbergenerate,args=(n,))
t1.name="AYAAN!"
t1.start()
print("how namy thread is active before jion() :{}".format(threading.active_count()))
t1.join()
print("how namy thread is active before jion().{}".format(threading.active_count()))
t1.name="AYAAN!"