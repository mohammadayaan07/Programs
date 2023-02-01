#threadingEx.py
import threading,time
def table(n):
    print("Table of {}".format(n))
    for i in range(1,11):
        print("{} X {} = {}".format(n,i,i*n))
t1=threading.Thread(target=table,args=(10,))
t2=threading.Thread(target=table,args=(11,))
t3=threading.Thread(target=table,args=(19,))
t1.start()
t2.start()
t3.start()
"""
threading.Thread(target.args)
active_count()
is_alive()
current_thread().name
threadobj.name="name"
lockobj=threading.Lock()
lockobj.acquire()
lockobj.release()
threading.Thread(target,args)
