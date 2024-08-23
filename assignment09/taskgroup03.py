import asyncio

async def task1():
    print('Hello from coroutine 1')
    await asyncio.sleep(1)
    
async def task2():
    print('Hello from coroutine 2')
    await asyncio.sleep(0.5)
    raise Exception('Something bad happened')

async def task3():
    print('Heoll from coroutine 2')
    await asyncio.sleep(1)