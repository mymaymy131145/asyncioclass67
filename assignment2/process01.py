
import multiprocessing  # นำเข้าโมดูล multiprocessing เพื่อใช้ในการประมวลผลขนาน
import os  # นำเข้าโมดูล os เพื่อใช้ฟังก์ชันที่เกี่ยวข้องกับระบบปฏิบัติการ
from time import sleep, ctime, time  # นำเข้าฟังก์ชัน sleep, ctime และ time จากโมดูล time

def cooking(index):  # กำหนดฟังก์ชันชื่อ cooking ที่รับค่า index เป็นพารามิเตอร์
    cooking_time = time()  # บันทึกเวลาเริ่มต้นการทำอาหาร
    print(f'{ctime()} Kitchen-{index}   : Begin cooking...PID {os.getpid()}')  # แสดงข้อความเริ่มการทำอาหาร พร้อมเวลาปัจจุบันและ PID
    sleep(2)  # หยุดการทำงานของโปรแกรมเป็นเวลา 2 วินาที
    duration = time() - cooking_time  # คำนวณระยะเวลาที่ใช้ในการทำอาหาร
    print(f'{ctime()} Kitchen-{index}   : Cooking done in {duration:0.2f} seconds!')  # แสดงข้อความการทำอาหารเสร็จสิ้น พร้อมเวลาที่ใช้

def kitchen(index):  # กำหนดฟังก์ชันชื่อ kitchen ที่รับค่า index เป็นพารามิเตอร์
    cooking(index)  # เรียกใช้ฟังก์ชัน cooking ด้วยค่า index ที่รับมา

if __name__ == "__main__":  # ตรวจสอบว่าโปรแกรมถูกเรียกใช้โดยตรง ไม่ได้ถูกนำเข้าเป็นโมดูล
    # Begin of main thread
    print(f'{ctime()} Main      : Start Cooking...PID {os.getpid()}')  # แสดงข้อความเริ่มต้นการทำอาหาร พร้อมเวลาปัจจุบันและ PID
    start_time = time()  # บันทึกเวลาเริ่มต้น

    # Multi kitchens with each chef
    kitchens = list()  # สร้างลิสต์เปล่าชื่อ kitchens
    for index in range(100):  # ลูปสองครั้งสำหรับสร้างกระบวนการทำอาหาร 2 กระบวนการ
        p = multiprocessing.Process(target=kitchen, args=(index,))  # สร้างกระบวนการทำอาหารใหม่ โดยกำหนดให้ฟังก์ชัน kitchen ทำงาน
        kitchens.append(p)  # เพิ่มกระบวนการทำอาหารใหม่ลงในลิสต์ kitchens
        # starting processes
        p.start()  # เริ่มการทำงานของกระบวนการทำอาหาร

    for index, p in enumerate(kitchens):  # ลูปผ่านกระบวนการทำอาหารทั้งหมด
        # wait until processes are finished
        p.join()  # รอจนกว่ากระบวนการทำอาหารทั้งหมดจะเสร็จสิ้น

    duration = time() - start_time  # คำนวณระยะเวลาที่ใช้ในการทำอาหารทั้งหมด
    print(f'{ctime()} Main      : Finished Cooking duration in {duration:0.2f} seconds')  # แสดงข้อความเสร็จสิ้นการทำอาหาร พร้อมเวลาที่ใช้
