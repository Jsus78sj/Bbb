import asyncio
import sys

# إنشاء حلقة أحداث (ضروري لبايثون 3.14+)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

import config
from config import Client

async def main():
    try:
        async with Client:
            print("✅ البوت يعمل...")
            # الحفاظ على البوت حيًا
            while True:
                await asyncio.sleep(3600)
    except Exception as e:
        print(f"❌ خطأ: {e}")
        sys.exit(1)

if __name__ == "__main__":
    loop.run_until_complete(main())
