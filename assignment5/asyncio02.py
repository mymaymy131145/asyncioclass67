# example of waiting for the first task to complete
from random import random  
# นำเข้าโมดูล random เพื่อใช้งานฟังก์ชัน random
import asyncio 
# นำเข้าโมดูล asyncio เพื่อใช้สำหรับการทำงานแบบอะซิงโครนัส

# coroutine ที่จะรันในงานใหม่
async def task_coro(arg): 
    # นิยามฟังก์ชันอะซิงโครนัสชื่อ task_coro ที่รับพารามิเตอร์ arg
    # สร้างค่าแบบสุ่มระหว่าง 0 และ 1
    value = random()  
    # สร้างตัวเลขสุ่มระหว่าง 0 และ 1 และเก็บไว้ในตัวแปร value
    # หยุดการทำงานชั่วคราว
    await asyncio.sleep(value)
    # รอเวลาตามค่าที่สุ่มได้ (value) โดยใช้ asyncio.sleep ซึ่งเป็นการหยุดแบบอะซิงโครนัส
    # รายงานค่า
    print(f'>task {arg} done with {value}') 
    # แสดงข้อความบอกว่างาน (task) หมายเลข arg เสร็จสิ้นพร้อมกับค่าที่สุ่มได้ (value)

# coroutine หลัก
async def main(): 
    # นิยามฟังก์ชันอะซิงโครนัสหลักชื่อ main
    # สร้างงานหลายงาน
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)] 
    # สร้างรายการของ tasks โดยสร้าง task_coro(i) สำหรับค่า i ตั้งแต่ 0 ถึง 9
    # รอให้งานแรกเสร็จ
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)  
    # รอให้งานใดงานหนึ่งใน tasks เสร็จ และเก็บผลลัพธ์ไว้ใน done และ pending
    # รายงานผลลัพธ์
    print('Done')
    # แสดงข้อความว่าเสร็จแล้ว
    # ดึงงานแรกที่เสร็จสิ้น
    first = done.pop()  # นำงานแรกที่เสร็จสิ้นออกจาก done
    print(first)  # แสดงข้อมูลของงานแรกที่เสร็จสิ้น

# เริ่มโปรแกรม asyncio
asyncio.run(main())  # รันฟังก์ชัน main() โดยใช้ asyncio
