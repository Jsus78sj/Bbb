import config
from config import Client
import os
import asyncio
from aiohttp import web

# معالج بسيط لأي طلب (فقط لإبقاء Render سعيدًا)
async def handle(request):
    return web.Response(text="Bot is running")

# تشغيل خادم الويب على المنفذ الذي يطلبه Render
async def run_web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"🌐 Web server started on port {port}")
    # حلقة لانهاية حتى لا تتوقف المهمة
    while True:
        await asyncio.sleep(3600)

async def main():
    # تشغيل الخادم في مهمة خلفية
    asyncio.create_task(run_web_server())
    
    # تشغيل البوت (باستخدام async context manager)
    async with Client:
        print("✅ البوت يعمل...")
        # انتظار لا نهائي (يدويًا بدل Client.idle())
        while True:
            await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
