import threading
import time
def task(lock):
    with lock:
        print(f"{threading.current_thread().name} has acquired the resource")
        time.sleep(2)
        print(f"{threading.current_thread().name} has released the resource")
lock=threading.Lock()
threads = []
for i in range(5):  
    thread = threading.Thread(target=task, args=(lock,), name=f"Thread-{i+1}")
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("All threads have completed execution.")        