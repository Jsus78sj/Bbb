import asyncio, os, glob, sys

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

import config
from config import Client

# حذف أي جلسات قديمة
for f in glob.glob("my_bot*"):
    try:
        os.remove(f)
    except:
        pass

async def main():
    try:
        async with Client:
            print("✅ البوت يعمل...")
            while True:
                await asyncio.sleep(3600)
    except Exception as e:
        print(f"❌ خطأ: {e}")
        sys.exit(1)

if __name__ == "__main__":
    loop.run_until_complete(main())
