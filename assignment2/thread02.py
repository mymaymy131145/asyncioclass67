# Thread version of cooking 1 kitchen 1 chefs 1 dishes
# Synchronous cooking
# 2 kitchen 2 chefs 2 dishes
import os
from time import time, ctime, sleep
import threading

def cooking(index):
    # การทำอาหารเริ่มต้น
    print(f'{ctime()} Kitchen-{index}  : Begin cooking...')
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index}  : Begin cooking...')
    sleep(2)
    duration = time() - cooking_time
    # การทำอาหารเสร็จสิ้น
    print(f'{ctime()} Kitchen-{index}  : Cooking done in {duration:0.2f} seconds!')

if __name__ == "__main__":
    # เริ่มต้นเธรดหลัก
    print(f'{ctime()} Main : Starting cook.')
    start_time = time()
    print(f"{ctime()} Main : ID of main process: {os.getpid()}")

    # การทำอาหารแบบมัลติเธรด
