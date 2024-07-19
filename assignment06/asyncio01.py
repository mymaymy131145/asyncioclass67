import time  # นำเข้าโมดูล time เพื่อใช้ฟังก์ชันที่เกี่ยวข้องกับเวลา

class Coffee:
    pass  # คลาส Coffee ใช้เป็นตัวแทนของกาแฟ แต่ไม่ทำอะไรในปัจจุบัน

class Egg:
    pass  # คลาส Egg ใช้เป็นตัวแทนของไข่ แต่ไม่ทำอะไรในปัจจุบัน

class Bacon:
    pass  # คลาส Bacon ใช้เป็นตัวแทนของเบคอน แต่ไม่ทำอะไรในปัจจุบัน

class Toast:
    pass  # คลาส Toast ใช้เป็นตัวแทนของขนมปังปิ้ง แต่ไม่ทำอะไรในปัจจุบัน

class Juice:
    pass  # คลาส Juice ใช้เป็นตัวแทนของน้ำผลไม้ แต่ไม่ทำอะไรในปัจจุบัน

def PourCoffee():
    print(f"{time.ctime()} - Begin pour coffee...")  # แสดงเวลาปัจจุบันและข้อความว่าเริ่มเทกาแฟ
    time.sleep(2)  # หยุดการทำงานเป็นเวลา 2 วินาที จำลองเวลาที่ใช้ในการเทกาแฟ
    print(f"{time.ctime()} - Finish pour coffee...")  # แสดงเวลาปัจจุบันและข้อความว่าเสร็จสิ้นการเทกาแฟ
    return Coffee()  # คืนค่าอ็อบเจ็กต์ของคลาส Coffee

def ApplyButter():
    print(f"{time.ctime()} - Begin apply butter...")  # แสดงเวลาปัจจุบันและข้อความว่าเริ่มทาเนย
    time.sleep(1)  # หยุดการทำงานเป็นเวลา 1 วินาที จำลองเวลาที่ใช้ในการทาเนย
    print(f"{time.ctime()} - Finish apply butter...")  # แสดงเวลาปัจจุบันและข้อความว่าเสร็จสิ้นการทาเนย


def FryEggs(eggs):
    print(f"{time.ctime()} - Begin fry eggs...")  # แสดงเวลาปัจจุบันและข้อความว่าเริ่มทอดไข่
    print(f"{time.ctime()} - Heat pan to fry eggs")  # แสดงเวลาปัจจุบันและข้อความว่าเริ่มทำให้กระทะร้อน
    time.sleep(1)  # หยุดการทำงานเป็นเวลา 1 วินาที จำลองการเตรียมกระทะ
    for egg in range(eggs):  # ลูปผ่านจำนวนไข่ที่ต้องทอด
        print(f"{time.ctime()} - Frying", egg+1, "eggs")  # แสดงเวลาปัจจุบันและข้อความว่าเริ่มทอดไข่ฟองที่กำหนด
        time.sleep(1)  # หยุดการทำงานเป็นเวลา 1 วินาที สำหรับแต่ละฟองไข่
    print(f"{time.ctime()} - Finish fry eggs...")  # แสดงเวลาปัจจุบันและข้อความว่าเสร็จสิ้นการทอดไข่
    print(f"{time.ctime()} - >>>>>>> Fry eggs are ready...")  # แสดงข้อความเพิ่มเติมว่าไข่ทอดพร้อมแล้ว
    return Egg()  # คืนค่าอ็อบเจ็กต์ของคลาส Egg

import time

class Coffee:
    pass

class Egg:
    pass

class Bacon:
    pass

class Toast:
    pass

class Juice:
    pass

def PourCoffee():
    print(f"{time.ctime()} - Begin pour coffee...")
    time.sleep(2)
    print(f"{time.ctime()} - Finish pour coffee...")
    return Coffee()

def ApplyButter():
    print(f"{time.ctime()} - Begin apply butter...")
    time.sleep(1)
    print(f"{time.ctime()} - Finish apply butter...")
    return Toast()  # Assuming ApplyButter returns Toast

def FryEggs(eggs):
    print(f"{time.ctime()} - Begin fry eggs...")
    print(f"{time.ctime()} - Heat pan to fry eggs")
    time.sleep(1)
    for egg in range(eggs):
        print(f"{time.ctime()} - Frying", egg + 1, "eggs")
        time.sleep(1)
    print(f"{time.ctime()} - Finish fry eggs...")
    print(f"{time.ctime()} - >>>>>>> Fry eggs are ready...")
    return Egg()

def FryBacon():
    print(f"{time.ctime()} - Begin fry bacon...")
    time.sleep(2)
    print(f"{time.ctime()} - Finish fry bacon...")
    print(f"{time.ctime()} - >>>>>>> Fry bacon is ready...")
    return Bacon()

def ToastBread(slices):
    for slice in range(slices):
        print(f"{time.ctime()} - Toasting bread", slice + 1)
        time.sleep(1)
        print(f"{time.ctime()} - Bread", slice + 1, "toasted")
        ApplyButter()
        print(f"{time.ctime()} - Toast", slice + 1, "ready")
    print(f"{time.ctime()} - >>>>>>> Toast are ready\n")
    return Toast()

def PourJuice():
    print(f"{time.ctime()} - Begin pour juice...")
    time.sleep(1)
    print(f"{time.ctime()} - Finish pour juice...")
    return Juice()

def main():
    PourCoffee()
    print(f"{time.ctime()} - >>>>>>> Coffee is ready\n")
    FryEggs(2)
    FryBacon()
    ToastBread(2)
    print(f"{time.ctime()} - >>>>>>> Nearly to finished...")
    PourJuice()

if __name__ == "__main__":
    start_cooking = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start_cooking
    print(f"{time.ctime()} - Breakfast cooked in ", elapsed, "seconds.")
