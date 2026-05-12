import config
from config import Client

if __name__ == "__main__":
    with Client:
        # يمكن وضع إعدادات إضافية هنا
        print("✅ البوت يعمل...")
        Client.run()
