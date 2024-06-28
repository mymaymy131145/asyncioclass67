# example of creating an event loop
#import asyncio

#loop = asyncio.new_event_loop()
#print(loop)

import asyncio

# สร้าง event loop ใหม่
loop = asyncio.new_event_loop()

# พิมพ์ object ของ event loop ที่ถูกสร้างขึ้นมา
print(loop)
