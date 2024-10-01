# # import random
# # import time

# # class SolarCell:
# #     def __init__ (self, id):
# #         self.id = id
# #         self.hardware_readtime = random.randint(1,3)
# #         print(f"Solar Cell {id} hardwre speed: {self.hardware_readtime}")
        
# #     def read_voltage(self):
# #         voltage = round(random.uniform(3.2, 6.0), 2)
# #         time.sleep(self.hardware_readtime)
# #         return voltage
    
# # def read_from_solar_cell(solar_solar):
# #     try: 
# #         while True:
# #             for solar_cell in solar_cell:
# #                 voltage = solar_cell.read_voltage()
# #                 print(f"{time.ctime()} Solar Cell #{SolarCell.id} Voltage: {voltage} V")
# #     except KeyboardInterrupt:
# #         print("\nโปรแกรมหยุดทำงาน.")
        
# # if __name__== "__main__":
# #     num_cells = 1 # กำหนดจำนวณแผงโซล่าเซลล์
# #     print(f"จำนวนแผลโซล่าเซลล์")
    
# #     sor_cells =  [SolarCell(i+1) for i in range(num_cells)]
# #     read_from_solar_cell(sor_cells)
    
# #     # จงพัฒนาโปรแกรมให้สามารถอ่านค่าแรงดันได้จากแผงโซล่าเซลแบบอะซิงโครนัส
# #     # และถ้าหากเพิ่มจำนวนแผงโซล่าเซลเป็น5แผง โปรแกรมที่พัฒนาแบบอะซิงโครนัสส่งผลอย่างไรบ้างจากผลลัพธ์ที่ได้



# import random
# import asyncio

# class SolarCell:
#     def __init__(self, id):
#         self.id = id
#         self.hardware_readtime = random.randint(1, 3)
#         print(f"Solar Cell {id} hardware speed: {self.hardware_readtime}")

#     async def read_voltage(self):
#         voltage = round(random.uniform(3.2, 6.0), 2)
#         await asyncio.sleep(self.hardware_readtime)
#         return voltage

# async def read_from_solar_cells(solar_cells):
#     try:
#         while True:
#             tasks = []
#             for solar_cell in solar_cells:
#                 tasks.append(read_solar_cell_voltage(solar_cell))
            
#             # Gather results asynchronously
#             await asyncio.gather(*tasks)
#     except KeyboardInterrupt:
#         print("\nโปรแกรมหยุดทำงาน.")

# async def read_solar_cell_voltage(solar_cell):
#     voltage = await solar_cell.read_voltage()
#     print(f"{time.ctime()} Solar Cell #{solar_cell.id} Voltage: {voltage} V")

# if __name__ == "__main__":
#     num_cells = 5  # เพิ่มจำนวนแผงโซล่าเซลล์
#     print(f"จำนวนแผงโซล่าเซลล์: {num_cells}")
    
#     solar_cells = [SolarCell(i+1) for i in range(num_cells)]
    
#     # Run the event loop
#     asyncio.run(read_from_solar_cells(solar_cells))






import random
import asyncio
import time  # เพิ่มการ import โมดูล time

class SolarCell:
    def __init__(self, id):
        self.id = id
        self.hardware_readtime = random.randint(1, 3)
        print(f"Solar Cell {id} hardware speed: {self.hardware_readtime}")

    async def read_voltage(self):
        voltage = round(random.uniform(3.2, 6.0), 2)
        await asyncio.sleep(self.hardware_readtime)
        return voltage

async def read_from_solar_cells(solar_cells):
    try:
        while True:
            tasks = []
            for solar_cell in solar_cells:
                tasks.append(read_solar_cell_voltage(solar_cell))
            
            # Gather results asynchronously
            await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        print("\nโปรแกรมหยุดทำงาน.")

async def read_solar_cell_voltage(solar_cell):
    voltage = await solar_cell.read_voltage()
    print(f"{time.ctime()} Solar Cell #{solar_cell.id} Voltage: {voltage} V")

if __name__ == "__main__":
    num_cells = 5  # เพิ่มจำนวนแผงโซล่าเซลล์
    print(f"จำนวนแผงโซล่าเซลล์: {num_cells}")
    
    solar_cells = [SolarCell(i+1) for i in range(num_cells)]
    
    # Run the event loop
    asyncio.run(read_from_solar_cells(solar_cells))
