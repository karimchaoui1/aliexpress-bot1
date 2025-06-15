
import requests

# توكن البوت وقناة النشر
TOKEN = "7915633089:AAG_cT_AEN0VXHTDno39F9eGH6LFGRCK0sg"
CHANNEL_ID = "@GetBestprices"

# رابط لمنتجات من AliExpress بصيغة JSON أو RSS تم توليدها سابقاً
PRODUCTS = [
    {
        "title": "🔥 Flash Deal: Wireless Earbuds",
        "link": "https://s.click.aliexpress.com/e/_on7Rdvk",
        "image": "https://ae01.alicdn.com/kf/HTb1.jpg"
    },
    {
        "title": "⭐ USB Charging Station - Limited Time Offer",
        "link": "https://s.click.aliexpress.com/e/_oEQ1sZk",
        "image": "https://ae01.alicdn.com/kf/HTb2.jpg"
    }
]

def send_to_telegram(product):
    text = f"{product['title']}\n\n🔗 [Buy Now]({product['link']})"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage", data=payload)

    # إرسال الصورة
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        data={"chat_id": CHANNEL_ID, "photo": product["image"]}
    )

def main():
    for product in PRODUCTS:
        send_to_telegram(product)

if __name__ == "__main__":
    main()
