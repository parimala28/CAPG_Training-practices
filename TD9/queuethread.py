import threading
import queue
import time

def producer(q):
    for i in range(5):
        item = f"Item {i}"  # Produce an item
        print(f"Producer produced: {item}")
        q.put(item)  # Add the item to the queue
        time.sleep(2)  # Simulate time taken to produce an item

def consumer(q):
    while True:
        item = q.get()  # Retrieve an item from the queue
        if item is None:  # Check for the sentinel value to stop the consumer
            break
        print(f"Consumer consumed: {item}")
        q.task_done()  # Mark the task as done

# Create a queue
q = queue.Queue()

# Create and start the producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(q,))
consumer_thread = threading.Thread(target=consumer, args=(q,))

producer_thread.start()
consumer_thread.start()

# Wait for the producer to finish producing items
producer_thread.join()

# Add a sentinel value to the queue to signal the consumer to stop
q.put(None)

# Wait for the consumer to finish processing all items
consumer_thread.join()

print("Thread communication completed")