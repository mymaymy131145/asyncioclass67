#import asyncio

#async def custom_coro():
 #   await asyncio.sleep(1)  # การใช้งานที่ถูกต้อง: เรียกใช้ asyncio.sleep พร้อมกับอาร์กิวเมนต์

#async def main():
 #   await custom_coro()

#asyncio.run(main())
import asyncio

# ตัวอย่าง coroutine ที่ใช้ asyncio.sleep
async def custom_coro():
    await asyncio.sleep(1)  # รอให้ผ่านไป 1 วินาที

# main coroutine ที่เรียกใช้ custom_coro
async def main():
    await custom_coro()  # เรียกใช้ coroutine custom_coro

asyncio.run(main())  # เรียกใช้ main coroutine ใน asyncio event loop

