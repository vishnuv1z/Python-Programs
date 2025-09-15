import threading, time

N=50_000_000

def count(n):
    x=0
    for i in range(n):
        x+=i

#Single thread
start=time.time()
count(N)
print("Single thread: ", time.time() - start)

#Two threads
start=time.time()
t1=threading.Thread(target=count, args=(N//2,))
t2=threading.Thread(target=count, args=(N//2,))
t1.start(); t2.start()
t1.join(); t2.join()
print("Two threads: ", time.time()-start)