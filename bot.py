import requests
import time

# بيانات البوت والقناة
TOKEN = "7915633089:AAG_cT_AEN0VXHTDno39F9eGH6LFGRCK0sg"
CHANNEL_ID = "@Bestfinds0"
AFFILIATE_KEY = "_okrQpFg"

# تحويل الرابط إلى أفلييت
def make_affiliate_link(product_url):
    return f"https://s.click.aliexpress.com/deep_link.htm?aff_short_key={AFFILIATE_KEY}&dl_target_url={product_url}"

# منتجات بصور صحيحة
PRODUCTS = [
    {
        "title": "🔥 Wireless Earbuds",
        "url": "https://www.aliexpress.com/item/1005006030907636.html",
        "image": "https://ae01.alicdn.com/kf/Sa2b91ae5055d43798234cb82cfc163afO.jpg"
    },
    {
        "title": "⭐ USB Charging Station",
        "url": "https://www.aliexpress.com/item/1005004825902045.html",
        "image": "https://ae01.alicdn.com/kf/Sf14211d203b247a7ae6ae205482a6165v.jpg"
    }
]

# إرسال المنشور
def send_to_telegram(product):
    affiliate_link = make_affiliate_link(product['url'])
    caption = f"{product['title']}\n\n🔗 [Buy Now]({affiliate_link})"
    payload = {
        "chat_id": CHANNEL_ID,
        "photo": product["image"],
        "caption": caption,
        "parse_mode": "Markdown"
    }

    response = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data=payload
    )

    if response.status_code != 200:
        print("❌ Error:", response.text)
    else:
        print("✅ Posted:", product['title'])

# تنفيذ تلقائي
def main():
    for product in PRODUCTS:
        send_to_telegram(product)
        time.sleep(10)

if __name__ == "__main__":
    main()
