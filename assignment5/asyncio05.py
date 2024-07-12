import asyncio
from random import random

# ฟังก์ชันสำหรับการทำข้าวผัด
async def cook_food(name):
    # สุ่มเวลาการทำข้าวผัดระหว่าง 1 ถึง 2 วินาที
    time_to_cook = 1 + random()
    
    print(f"Microwave ({name}): Cooking {time_to_cook} seconds..")
    # รอเวลาที่กำหนดเพื่อจำลองการทำข้าวผัด
    await asyncio.sleep(time_to_cook)
    # พิมพ์เวลาที่ใช้ในการทำข้าวผัด
    print(f"Microwave ({name}): Cooking finished")
    return name, time_to_cook# คืนค่า 'Rice' เมื่อการทำข้าวผัดเสร็จสิ้น



# ฟังก์ชันหลักที่จัดการการทำอาหาร
async def main():
    # สร้าง tasks สำหรับการทำอาหารแต่ละชนิด
    tasks = [
        asyncio.create_task(cook_food("rice")),   # สร้าง task สำหรับข้าวผัด
        asyncio.create_task(cook_food("noodle")), # สร้าง task สำหรับก๋วยเตี๋ยว
        asyncio.create_task(cook_food("curry"))   # สร้าง task สำหรับข้าวแกง
    ]
    
    # รอจนกว่า task แรกจะเสร็จ โดยใช้ return_when=asyncio.FIRST_COMPLETED
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print(f"Completed task:{len(done)}")
    
    completed_task = done.pop()
    
    meal, time_to_cook = await completed_task
    
    print(f" - {meal} is completed in {time_to_cook} seconds")
    
    print(f"Uncompleted task :{len(pending)}")
# เรียกใช้ฟังก์ชันหลักเพื่อเริ่มโปรแกรม
asyncio.run(main())
