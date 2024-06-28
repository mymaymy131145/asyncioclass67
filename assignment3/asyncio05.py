# When a coroutine is wrapped into a Task with functions like asyncio.create_task() the coroutine is automatically scheduled to run soon
import asyncio
import aiohttp

from time import ctime

async def get_api(client, url):
    async with client.get(url) as response:
        return await response.json()

async def fetch_hacker_news():
    async with aiohttp.ClientSession() as session:
        url1 = "https://hacker-news.firebaseio.com/v0/item/24661271.json?print=pretty"
        url2 = "https://hacker-news.firebaseio.com/v0/item/24659683.json?print=pretty"

        task1 = asyncio.create_task(get_api(session, url1))
        task2 = asyncio.create_task(get_api(session, url2))

        news1 = await task1  # รอจนกว่า task 1 จะเสร็จสิ้น
        news2 = await task2  # รอจนกว่า task 2 จะเสร็จสิ้น

        print(f"{ctime()} {news1['title']}")
        print(f"{ctime()} {news2['title']}")

asyncio.run(fetch_hacker_news())
