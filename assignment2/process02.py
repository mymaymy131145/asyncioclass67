# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# share resources
import multiprocessing  # นำเข้าโมดูล multiprocessing เพื่อใช้ในการประมวลผลขนาน
import os  # นำเข้าโมดูล os เพื่อใช้ฟังก์ชันที่เกี่ยวข้องกับระบบปฏิบัติการ
from time import sleep, ctime, time  # นำเข้าฟังก์ชัน sleep, ctime และ time จากโมดูล time

# Basket of sharing
class Basket:  # กำหนดคลาสชื่อ Basket
    def __init__(self):  # เมธอดตัวสร้างสำหรับคลาส Basket
        self.eggs = 50  # กำหนดจำนวนไข่ในตะกร้าเริ่มต้นเป็น 50
    def use_eggs(self, index):  # กำหนดเมธอด use_eggs ที่รับค่า index เป็นพารามิเตอร์
        print(f'{ctime()} Kitchen-{index}   : Chef-{index} has lock with eggs remaining {self.eggs}')  # แสดงข้อความการล็อคตะกร้าพร้อมจำนวนไข่ที่เหลืออยู่
        self.eggs -= 1  # ลดจำนวนไข่ลง 1
        print(f'{ctime()} Kitchen-{index}   : Chef-{index} has released lock with eggs remaining {self.eggs}')  # แสดงข้อความการปลดล็อคตะกร้าพร้อมจำนวนไข่ที่เหลืออยู่

# Chef cooking
def cooking(index, basket):  # กำหนดฟังก์ชันชื่อ cooking ที่รับค่า index และ basket เป็นพารามิเตอร์
    basket.use_eggs(index)  # เรียกใช้เมธอด use_eggs จากคลาส Basket
    sleep(2)  # หยุดการทำงานของโปรแกรมเป็นเวลา 2 วินาที

# Kitchen cooking
def kitchen(index, share_eggs):  # กำหนดฟังก์ชันชื่อ kitchen ที่รับค่า index และ share_eggs เป็นพารามิเตอร์
    print(f'{ctime()} Kitchen-{index}   : Begin cooking...PID {os.getpid()}')  # แสดงข้อความเริ่มการทำอาหาร พร้อมเวลาปัจจุบันและ PID
    cooking_time = time()  # บันทึกเวลาเริ่มต้นการทำอาหาร
    cooking(index, share_eggs)  # เรียกใช้ฟังก์ชัน cooking ด้วยค่า index และ share_eggs
    duration = time() - cooking_time  # คำนวณระยะเวลาที่ใช้ในการทำอาหาร
    print(f'{ctime()} Kitchen-{index}   : Cooking done in {duration:0.2f} seconds!')  # แสดงข้อความการทำอาหารเสร็จสิ้น พร้อมเวลาที่ใช้

if __name__ == "__main__":  # ตรวจสอบว่าโปรแกรมถูกเรียกใช้โดยตรง ไม่ได้ถูกนำเข้าเป็นโมดูล
    # Begin of main thread
    print(f'{ctime()} Main      : Start Cooking...PID {os.getpid()}')  # แสดงข้อความเริ่มต้นการทำอาหาร พร้อมเวลาปัจจุบันและ PID
    start_time = time()  # บันทึกเวลาเริ่มต้น

    basket = Basket()  # สร้างอินสแตนซ์ใหม่จากคลาส Basket

    # Multi processes
    kitchens = list()  # สร้างลิสต์เปล่าชื่อ kitchens
    for index in range(2):  # ลูปสองครั้งสำหรับสร้างกระบวนการทำอาหาร 2 กระบวนการ
        p = multiprocessing.Process(target=kitchen, args=(index, basket))  # สร้างกระบวนการทำอาหารใหม่ โดยกำหนดให้ฟังก์ชัน kitchen ทำงาน
        kitchens.append(p)  # เพิ่มกระบวนการทำอาหารใหม่ลงในลิสต์ kitchens
        # starting processes
        p.start()  # เริ่มการทำงานของกระบวนการทำอาหาร

    for index, p in enumerate(kitchens):  # ลูปผ่านกระบวนการทำอาหารทั้งหมด
        # wait until processes are finished
        p.join()  # รอจนกว่ากระบวนการทำอาหารทั้งหมดจะเสร็จสิ้น

    print(f'{ctime()} Main      : Basket eggs remaining {basket.eggs}')  # แสดงจำนวนไข่ที่เหลืออยู่ในตะกร้า
    duration = time() - start_time  # คำนวณระยะเวลาที่ใช้ในการทำอาหารทั้งหมด
    print(f'{ctime()} Main      : Finished Cooking duration in {duration:0.2f} seconds')  # แสดงข้อความเสร็จสิ้นการทำอาหาร พร้อมเวลาที่ใช้
