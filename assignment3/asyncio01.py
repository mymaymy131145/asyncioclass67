# check the type of a coroutine
import asyncio

# กำหนดฟังก์ชันแบบอะซิงโครนัส
async def custom_coro():
    # จำลองการทำงาน I/O โดยใช้ asyncio.sleep
    await asyncio.sleep(1)

# สร้างวัตถุ coroutine โดยการเรียกฟังก์ชันแบบอะซิงโครนัส
coro = custom_coro()

# พิมพ์ประเภทของวัตถุ coroutine
print(type(coro))  # จะพิมพ์ <class 'coroutine'>
  