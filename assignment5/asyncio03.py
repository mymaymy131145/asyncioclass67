# example of waiting for the first task to fail
from random import random  # นำเข้าโมดูล random เพื่อใช้งานฟังก์ชัน random
import asyncio  # นำเข้าโมดูล asyncio เพื่อใช้สำหรับการทำงานแบบอะซิงโครนัส

# coroutine ที่จะรันในงานใหม่
async def task_coro(arg):  # นิยามฟังก์ชันอะซิงโครนัสชื่อ task_coro ที่รับพารามิเตอร์ arg
    # สร้างค่าแบบสุ่มระหว่าง 0 และ 1
    value = random()  # สร้างตัวเลขสุ่มระหว่าง 0 และ 1 และเก็บไว้ในตัวแปร value
    # หยุดการทำงานชั่วคราว
    await asyncio.sleep(value)  # รอเวลาตามค่าที่สุ่มได้ (value) โดยใช้ asyncio.sleep ซึ่งเป็นการหยุดแบบอะซิงโครนัส
    # รายงานค่า
    print(f'>task {arg} done with {value}')  # แสดงข้อความบอกว่างาน (task) หมายเลข arg เสร็จสิ้นพร้อมกับค่าที่สุ่มได้ (value)
    # ล้มเหลวตามเงื่อนไข
    if value < 0.5:  # ถ้าค่าที่สุ่มได้น้อยกว่า 0.5
        raise Exception(f'Something bad happened in {arg}')  # ทำการโยนข้อผิดพลาด (Exception) พร้อมกับข้อความ

# coroutine หลัก
async def main():  # นิยามฟังก์ชันอะซิงโครนัสหลักชื่อ main
    # สร้างงานหลายงาน
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]  # สร้างรายการของ tasks โดยสร้าง task_coro(i) สำหรับค่า i ตั้งแต่ 0 ถึง 9
    # รอให้งานแรกที่ล้มเหลวหรือทุกงานเสร็จสิ้น
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)  # รอให้งานใดงานหนึ่งล้มเหลวหรือทุกงานเสร็จ และเก็บผลลัพธ์ไว้ใน done และ pending
    # รายงานผลลัพธ์
    print('Done')  # แสดงข้อความว่าเสร็จแล้ว
    # ดึงงานแรกที่ล้มเหลว
    first = done.pop()  # นำงานแรกที่เสร็จสิ้นออกจาก done
    print(first)  # แสดงข้อมูลของงานแรกที่เสร็จสิ้น

# เริ่มโปรแกรม asyncio
asyncio.run(main())  # รันฟังก์ชัน main() โดยใช้ asyncio
