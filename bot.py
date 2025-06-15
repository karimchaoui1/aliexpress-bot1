
import requests

# توكن البوت وقناة النشر
TOKEN = "7915633089:AAG_cT_AEN0VXHTDno39F9eGH6LFGRCK0sg"
CHANNEL_ID = "@GetBestprices"

# مفتاح الأفلييت
AFFILIATE_KEY = "_okrQpFg"

# دالة لإنشاء رابط أفلييت تلقائي من رابط منتج عادي
def make_affiliate_link(product_url):
    return "https://s.click.aliexpress.com/deep_link.htm?aff_short_key=" + AFFILIATE_KEY + "&dl_target_url=" + product_url

# المنتجات (بروابط علي إكسبريس العادية)
PRODUCTS = [
    {
        "title": "🔥 Wireless Earbuds",
        "link": make_affiliate_link("https://www.aliexpress.com/item/1005006030907636.html"),
        "image": "https://ae01.alicdn.com/kf/HTb1.jpg"
    },
    {
        "title": "⭐ USB Charging Station",
        "link": make_affiliate_link("https://www.aliexpress.com/item/1005004825902045.html"),
        "image": "https://ae01.alicdn.com/kf/HTb2.jpg"
    }
]

# إرسال رسالة نصية مع روابط
def send_to_telegram(product):
    caption = (
        product['title'] + "\n\n"
        "🖼️ Product Image: " + product['image'] + "\n"
        "🔗 [Buy Now](" + product['link'] + ")"
    )

    payload = {
        "chat_id": CHANNEL_ID,
        "text": caption,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }

    response = requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data=payload
    )

    if response.status_code != 200:
        print("❌ Error:", response.text)

def main():
    for product in PRODUCTS:
        send_to_telegram(product)

if __name__ == "__main__":
    main()
