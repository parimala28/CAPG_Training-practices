import threading
Lists =[
    list(range(260)),
    list(range(260,300))
]
def process_data(Lists):
    res=sum(Lists)
    print(f"The sum is: {res}")
threads=[]
for Chunks in Lists:
    th=threading.Thread(target=process_data,args=(Chunks,))
    threads.append(th)
    th.start()
for th in threads:
    th.join()       