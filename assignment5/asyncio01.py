# example of waiting for all tasks to complete
# example of waiting for the first task to complete
# ตัวอย่างการรอให้งานแรกเสร็จสมบูรณ์

from random import random  # นำเข้าฟังก์ชัน random จากโมดูล random
import asyncio  # นำเข้าโมดูล asyncio สำหรับการเขียนโปรแกรมแบบอะซิงโครนัส

# coroutine to execute in a new task
# coroutine ที่จะถูกเรียกใช้ในงานใหม่

async def task_coro(arg):  # นิยามฟังก์ชัน coroutine ชื่อ task_coro ที่รับพารามิเตอร์ arg
    # generate a random value between 0 and 1
    # สร้างค่าตัวเลขสุ่มระหว่าง 0 ถึง 1
    value = random()  # สร้างตัวเลขสุ่มระหว่าง 0 ถึง 1
    # block for a moment
    # หยุดทำงานชั่วคราว
    await asyncio.sleep(value)  # หยุดทำงานแบบอะซิงโครนัสเป็นเวลาตามค่าตัวเลขสุ่มที่สร้างได้
    # report the value
    # รายงานค่า
    print(f'>task {arg} done with {value}')  # พิมพ์หมายเลขงานและค่าที่ได้จากการสุ่ม

# main coroutine
# coroutine หลัก

async def main():  # นิยามฟังก์ชัน coroutine ชื่อ main
    # create many tasks
    # สร้างงานหลายงาน
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]  # สร้างรายการของงาน coroutine จำนวน 10 งาน โดยใช้ task_coro และสร้างงานด้วย asyncio.create_task()
    # wait for the first task to complete
    # รอให้งานแรกเสร็จสมบูรณ์
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # รอให้งานในรายการเสร็จงานแรก โดยใช้ asyncio.wait() และเก็บผลลัพธ์ใน done และ pending
    # report result
    # รายงานผลลัพธ์
    print('Done')  # พิมพ์คำว่า 'Done'
    # get the first task to complete
    # รับงานที่เสร็จสมบูรณ์งานแรก
    first = done.pop()  # นำงานแรกที่เสร็จสมบูรณ์ออกจากรายการ done
    print(first)  # พิมพ์งานแรกที่เสร็จสมบูรณ์

# start the asyncio program
# เริ่มโปรแกรม asyncio
asyncio.run(main())  # เรียกใช้ฟังก์ชัน main() ด้วย asyncio.run()
