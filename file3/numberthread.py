#numberthread.py
import threading,time
class even:
    def even(n):
        for val in range(2,n+1,2):
            print("{}---->{}".format(threading.current_thread().name,val))
            time.sleep(1)
class odd:
    def odd(n):
        for val in range(1,n+1,2):
            print("\n{}---->{}".format(threading.current_thread().name,val))
            time.sleep(1)
ev=even()
t1=threading.Thread(target=ev.even(),args=(10,))
t1.name="even"
od=odd()
t2=threading.Thread(target=od.odd(),args=(10,))
t2.name="odd"
t1.start()
t2.start()
print(threading.active_count())
t1.join()
t2.join()