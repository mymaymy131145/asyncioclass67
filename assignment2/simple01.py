# Synchronous cooking
# 1 kitchen 1 chefs 1 dish
from time import sleep, ctime, time  # นำเข้าฟังก์ชัน sleep, ctime และ time จากโมดูล time

# Cooking synchronous
def cooking(index):  # กำหนดฟังก์ชันชื่อ cooking ที่รับค่า index เป็นพารามิเตอร์
    print(f'{ctime()} Kitchen-{index}   : Begin cooking...')  # แสดงข้อความเริ่มการทำอาหาร พร้อมเวลาปัจจุบัน
    sleep(2)  # หยุดการทำงานของโปรแกรมเป็นเวลา 2 วินาที
    print(f'{ctime()} Kitchen-{index}   : Cooking done!')  # แสดงข้อความการทำอาหารเสร็จสิ้น พร้อมเวลาปัจจุบัน

if __name__ == "__main__":  # ตรวจสอบว่าโปรแกรมถูกเรียกใช้โดยตรง ไม่ได้ถูกนำเข้าเป็นโมดูล
    # Begin of main thread
    print(f'{ctime()} Main      : Start Cooking.')  # แสดงข้อความเริ่มต้นการทำอาหาร พร้อมเวลาปัจจุบัน
    start_time = time()  # บันทึกเวลาเริ่มต้น
    # Cooking
    cooking(0)  # เรียกใช้ฟังก์ชัน cooking ด้วยค่า index เท่ากับ 0

    duration = time() - start_time  # คำนวณระยะเวลาที่ใช้ในการทำอาหาร
    print(f'{ctime()} Main      : Finished Cooking duration in {duration:0.2f} seconds')  # แสดงข้อความเสร็จสิ้นการทำอาหาร พร้อมเวลาที่ใช้
