# Import libraries
import multiprocessing
from multiprocessing import Value
import os
from time import sleep, ctime, time

# Class for basket of eggs
class Basket:
    def __init__(self, eggs):
        self.eggs = Value('i', eggs)  # Shared memory for eggs count

    def use_eggs(self, index):
        # Lock to prevent race conditions when modifying shared eggs count
        with self.eggs.get_lock():
            self.eggs.value -= 1  # Decrement eggs count

        # Print a message about the chef, kitchen and remaining eggs
        print(f"{ctime()} Kitchen-{index}: Chef-{index} has locked with eggs remaining {self.eggs.value}")
        sleep(0.2)  # Simulate cooking time
        print(f"{ctime()} Kitchen-{index}: Chef-{index} has released lock with eggs remaining {self.eggs.value}")

# Cooking function
def cooking(index, basket):
    cooking_time = time()
    print(f"{ctime()} Kitchen-{index}: Begin cooking... PID {os.getpid()}")
    sleep(2)  # Simulate cooking time
    duration = time() - cooking_time

    # Lock to prevent race conditions when modifying shared eggs count
    with basket.eggs.get_lock():
        basket.use_eggs(index)  # Decrement eggs count and print a message

    # Print a message about cooking time
    print(f"{ctime()} Kitchen-{index}: Cooking done in {duration:.2f} seconds!")


# Kitchen function
def kitchen(index, basket):
    cooking(index, basket)


# Main function
if __name__ == "__main__":
    # Print program start time
    print(f"{ctime()} Main: Begin Cooking.")
    start_time = time()

    # Create a basket of eggs
    basket = Basket(50)

    # Print the main process ID
    print(f"{ctime()} Main: ID of main process: {os.getpid()}")

    # Create and start child processes
    kitchens = []
    for index in range(2):
        p = multiprocessing.Process(target=kitchen, args=(index, basket))
        p.start()
        kitchens.append(p)

    # Wait for child processes to finish
    for p in kitchens:
        p.join()

    # Print the remaining eggs and total cooking duration
    duration = time() - start_time
    print(f"{ctime()} Main: Basket eggs remaining {basket.eggs.value}")
    print(f"{ctime()} Main: Finished Cooking in {duration:.2f} seconds")
