# example of waiting for all tasks to be completed with a timeout
from random import random
import asyncio

#coroutine to execute in a new task
async def task_coro(arg):
    #generate a random value between 6 and 16
    value = random() * 10 

    #block for a moment
    await asyncio.sleep(value)

    #report the value
    print(f'>task ({arg}) done with ({value})')
    
async def main():
    tasks = [asyncio.create_task(task_coro(i) for i in range(10))]
    done,pending = await asyncio.wait(tasks, timeout=5)
    print(f'Done, {len(done)} tasks comleted in time')
    
asyncio.run(main())