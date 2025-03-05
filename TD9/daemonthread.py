import threading
import time
def Daemon_task():
    while True:
        print("Daemon thread running.....")
        time.sleep(5)
Daemon_thread=threading.Thread(target=Daemon_task,daemon=True)
Daemon_thread.start()  
time.sleep(10)        
print("main thread exiting") 