import requests
import time

# إعدادات البوت
BOT_TOKEN = "ضع_هنا_توكن_البوت"
CHANNEL_USERNAME = "@ضع_هنا_اسم_قناتك"
AFFILIATE_TAG = "https://s.click.aliexpress.com/e/_on7Rdvk"  # رابط أفلييت افتراضي

# جلب عروض AliExpress Flash Deals (نسخة مبسطة)
def fetch_flash_deals():
    try:
        response = requests.get("https://gw.alicdn.com/bao/uploaded/deal_feed_flash.json")
        data = response.json()
        return data.get("data", [])[0:3]  # نأخذ فقط 3 عروض
    except Exception as e:
        print("خطأ أثناء جلب البيانات:", e)
        return []

# إرسال الرسالة إلى قناة تليغرام
def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_USERNAME,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=payload)
    print(response.text)

# تنسيق ونشر العروض
def main():
    deals = fetch_flash_deals()
    if not deals:
        print("لا توجد عروض.")
        return
    for deal in deals:
        title = deal.get("title", "منتج")
        price = deal.get("price", "؟")
        img = deal.get("img", "")
        link = AFFILIATE_TAG
        message = f"🔥 <b>{title}</b>\n💰 السعر: {price} دولار\n🛒 <a href='{link}'>رابط الشراء</a>"
        send_to_telegram(message)
        time.sleep(5)  # مهلة بين الرسائل لتجنب الحظر

# تنفيذ المهمة
if __name__ == "__main__":
    main()