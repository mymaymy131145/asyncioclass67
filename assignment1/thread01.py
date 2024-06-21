# running a function in another thread
from time import sleep
from threading import Thread

def task():
    while True:
        print("This is from another thread")
        sleep(2)

thread = Thread(target=task)
thread.start()

print("Waiting for the thread...")
thread.join()
