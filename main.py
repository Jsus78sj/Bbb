import asyncio
import os

# إنشاء حلقة أحداث جديدة للخيط الرئيسي لتجنب خطأ Pyrogram
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

import config
from config import Client
from aiohttp import web

# خادم ويب بسيط لمنع Render من إيقاف الخدمة
async def handle(request):
    return web.Response(text="Bot is running")

async def run_web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"🌐 Web server started on port {port}")
    # إبقاء المهمة حية
    while True:
        await asyncio.sleep(3600)

async def main():
    # تشغيل خادم الويب في الخلفية
    asyncio.create_task(run_web_server())
    
    # تشغيل بوت التليجرام
    async with Client:
        print("✅ البوت يعمل...")
        # إبقاء العملية نشطة
        while True:
            await asyncio.sleep(3600)

if __name__ == "__main__":
    # استخدام الحلقة التي أنشأناها سابقًا
    loop.run_until_complete(main())
