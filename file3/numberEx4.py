#numberEx4.py
import threading,time
class student:
	def generate(self,n):
		print("name of the thread in genrate()=",threading.current_thread().name)
		if(n<=0):
			print("invaild index")
		else:
			print("*"*40)
			print("NUMBER=",n)
			print("*"*40)
			for i in range(n,0,-1):
				print("\t{}".format(i))
				time.sleep(1)
			print("*"*40)
no=student()
t1=threading.Thread(target=no.generate,args=(int(input("Enter the Number:")),))
t1.name="AYAAN"
t1.start()
