'''Threading in Python
Threading in Python is used to run multiple tasks concurrently within the same process. 
The threading module allows you to create and manage threads easily.'''

'''1️⃣ What is a Thread?
A thread is the smallest unit of a process that can run independently. Python supports multithreading, 
but due to the Global Interpreter Lock (GIL), only one thread can execute Python bytecode at a time. 
This means Python threads are best used for I/O-bound tasks rather than CPU-heavy tasks.'''



# 2️⃣ Creating and Starting a Thread
# You can create a new thread using the threading.Thread class.

import threading

def print_numbers():
    for i in range(1,5):
        print("number:",i)

t=threading.Thread(target=print_numbers)

t.start()
print("Main Thread")

# 3️⃣ Joining a Thread (Waiting for Completion)
# If you want the main thread to wait for another thread to complete, use .join().

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)  # Simulate work
        print(f"Number: {i}")

t = threading.Thread(target=print_numbers)
t.start()

print("Waiting for the thread to finish...")
t.join()  # Main thread waits for t to finish
print("Thread finished!")


# 4️⃣ Running Multiple Threads

import threading
import time

def print_numbers(name):
    for i in range(1,3):
        time.sleep(1)
        print(f"{name}:{i}")

t1=threading.Thread(target=print_numbers,args=("Thread-1",))
t2=threading.Thread(target=print_numbers,args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread")


# 5️⃣ Using Thread with a Class

import threading

class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            print(f"Thread {self.name}:{i}")

t=MyThread()
t.start()
t.join()

print("main thread")

# 6️⃣ Thread Synchronization (Avoiding Race Conditions)
# When multiple threads access shared resources, race conditions can occur. Use a lock to prevent simultaneous access.

import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  # Ensures only one thread modifies `counter` at a time
            counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Counter:", counter)  # Should be 200000




