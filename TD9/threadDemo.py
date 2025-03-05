import threading  #1
import time        #2

def single_task():
    print("Task started") #4
    time.sleep(2)#5
    print("Task completed")#6
    
thread=threading.Thread(target=single_task)#3
thread.start()#4
thread.join()#7
print("Main thraed execute completed")#8