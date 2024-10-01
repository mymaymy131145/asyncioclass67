import asyncio
import time

data1 = [5, 2, 3, 1, 4]
data2 = [50, 30, 10, 20, 40]
data3 = [500, 300, 100, 200, 400]

async def process_data(data, delay):
    print(f"At t={time.time()-start:.2f} รอ {delay} วินาทีก่อนประมวลผลข้อมูลนี้...")
    await asyncio.sleep(delay)
    
    sorted_data = sorted(data)
    print(f"At t={time.time()-start:.2f} ข้อมูลที่เรียงลำดับ: {sorted_data}")
    return sorted_data

async def main():

    results = await asyncio.gather(
        process_data(data1, 2),
        process_data(data2, 3),
        process_data(data3, 1)
    )

    
    result1, result2, result3 = results

    print(f"At t={time.time()-start:.2f} ผลลัพธ์จาก data1: {result1}")
    print(f"At t={time.time()-start:.2f} ผลลัพธ์จาก data2: {result2}")
    print(f"At t={time.time()-start:.2f} ผลลัพธ์จาก data3: {result3}")

start = time.time()
asyncio.run(main())



### เหตุผลที่เลือกใช้ `gather`:
#1. **ทำงานพร้อมกัน**: `gather` ช่วยให้เราสามารถประมวลผลหลายงานพร้อมกันได้ในรูปแบบ asynchronous โดยไม่ต้องรอทีละงาน
#2. **สะดวกและเข้าใจง่าย**: เหมาะกับสถานการณ์ที่ต้องการผลลัพธ์ของ task ทั้งหมดในคราวเดียว
#3. **โครงสร้างเรียบง่าย**: ไม่ซับซ้อน เหมาะสำหรับงานที่ไม่ต้องการการจัดการข้อผิดพลาดหรือ task ที่ซับซ้อน