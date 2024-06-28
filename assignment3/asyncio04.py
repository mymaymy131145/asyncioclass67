from time import ctime
import asyncio

# นิยามฟังก์ชัน wash ที่ใช้ async/await
async def wash(basket):
    print(f"{ctime()} : Washing Machine ({basket}): Put the coin")

    # หยุดการทำงานเพื่อ simulating การล้าง 5 วินาที
    await asyncio.sleep(5)
    print(f"{ctime()} : Washing Machine ({basket}): Start washing...")

    # หยุดการทำงานเพื่อ simulating การล้าง 10 วินาที
    await asyncio.sleep(10)
    print(f"{ctime()} : {basket} is completed")
    print(f"{ctime()} : Washing Machine ({basket}): Finished washing")

# ฟังก์ชันหลักที่ใช้ asyncio
async def main():
    coro = wash("Basket A")  # เรียกใช้ wash function และระบุชื่อตะกร้า

    print(f"{ctime()} : {coro}")  # แสดงข้อความพร้อมกับการเรียกใช้ฟังก์ชัน

    task = asyncio.create_task(coro)  # สร้าง task จาก coroutine
    print(f"{ctime()} : {task}")  # แสดงข้อความพร้อมกับการเรียกใช้งาน task

    print(f"{ctime()} : {type(task)}")  # แสดงข้อความพร้อมกับการเรียกใช้งานชนิดของ task

    result = await task  # รอผลลัพธ์จากการทำงานของ task
    print(f"{ctime()} : {result}")  # แสดงข้อความพร้อมกับการเรียกใช้งานผลลัพธ์

if __name__ == "__main__":
    asyncio.run(main())  # เรียกใช้งานฟังก์ชันหลัก main ด้วย asyncio.run()
