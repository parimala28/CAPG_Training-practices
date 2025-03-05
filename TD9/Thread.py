import threading
import time

def even():
    for i in range(0,10,2):
        print("Even:",i)
        time.sleep(2)


def odd():
    for i in range(1,10,2):
        print("Odd:",i)
        time.sleep(2)

thread=threading.Thread(target=even)
thread1=threading.Thread(target=odd)
thread.start()
thread.join()
thread1.start()
thread1.join()
    
