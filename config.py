import os
from pyrogram import Client
import redis

# جلب القيم من متغيرات البيئة
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
REDIS_URL = os.getenv("REDIS_URL")  # رابط Redis (من Upstash مثلاً)
Dev_Zaid = os.getenv("DEV_ZAID", "6646631745")  # غيّره إلى معرف البوت أو معرف المطور

# إنشاء عميل Redis من الرابط
if REDIS_URL:
    r = redis.from_url(REDIS_URL, decode_responses=True)
else:
    r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

wsdb = r  # بعض أجزاء الكود تستخدم wsdb كاسم ثانٍ للـ Redis

# كائن البوت
Client = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Plugins")
)
