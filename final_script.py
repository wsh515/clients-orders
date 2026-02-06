import json
import os
import urllib.parse

# الإعدادات
GITHUB_BASE = "https://raw.githubusercontent.com/wsh515/clients-orders/main/"
JSON_INPUT = 'reviews.json'
JSON_OUTPUT = 'reviews_updated.json'

def update_json():
    if not os.path.exists(JSON_INPUT):
        print(f"❌ لم يتم العثور على {JSON_INPUT}!")
        return

    with open(JSON_INPUT, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for person in data:
        name = person.get('name')
        # التحقق من وجود المجلد على جهازك
        if name and os.path.isdir(name):
            image_urls = []
            files = sorted(os.listdir(name))
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                    # تشفير الاسم للروابط (خاصة للأسماء العربية والمسافات)
                    enc_name = urllib.parse.quote(name)
                    enc_file = urllib.parse.quote(file)
                    url = f"{GITHUB_BASE}{enc_name}/{enc_file}"
                    image_urls.append(url)
            
            person['images'] = image_urls
            print(f"✅ تم تحديث {name} بـ {len(image_urls)} صور")

    with open(JSON_OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"\n✨ انتهى! الملف الجديد هو: {JSON_OUTPUT}")

if __name__ == "__main__":
    update_json()