import requests

TOKEN = "7915633089:AAG_cT_AEN0VXHTDno39F9eGH6LFGRCK0sg"
CHANNEL_ID = "@Bestfinds0"
AFFILIATE_KEY = "_okrQpFg"

def make_affiliate_link(product_url):
    return f"https://s.click.aliexpress.com/deep_link.htm?aff_short_key={AFFILIATE_KEY}&dl_target_url={product_url}"

PRODUCTS = [
    {
        "title": "🔥 Wireless Earbuds",
        "url": "https://www.aliexpress.com/item/1005006030907636.html",
        "image": "https://ae01.alicdn.com/kf/HTb1.jpg"
    },
    {
        "title": "⭐ USB Charging Station",
        "url": "https://www.aliexpress.com/item/1005004825902045.html",
        "image": "https://ae01.alicdn.com/kf/HTb2.jpg"
    }
]

def send_to_telegram(product):
    affiliate_link = make_affiliate_link(product['url'])
    caption = product['title'] + "\n\n🔗 [Buy Now](" + affiliate_link + ")"
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

def main():
    for product in PRODUCTS:
        send_to_telegram(product)

if __name__ == "__main__":
    main()
