# running a function with arguments in another thread
#running a function with arguments in another thread
from time import sleep, ctime
from threading import Thread

#a custom function that blocks for a moment
def task():
    #block for a moment
    sleep(1)
    # dsplay a message
    print(f'{ctime()} This is from another therad')

#create a thread
thread = Thread(target=task)
#run the thread
thread.start()
#wait for the thread to finish
print(f'{ctime()} Waiting for the thread...')
thread.join()