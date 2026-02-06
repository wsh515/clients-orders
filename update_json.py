import json
import os
import urllib.parse

# الإعدادات الأساسية
GITHUB_BASE_URL = "https://raw.githubusercontent.com/wsh515/clients-orders/main/"
JSON_FILE = 'reviews.json'
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp')

def update_reviews():
    # 1. تحميل ملف JSON الأصلي
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. المرور على كل شخص في الملف
    for person in data:
        name = person.get('name')
        if name and os.path.isdir(name):
            image_urls = []
            
            # الحصول على الصور داخل مجلد الشخص وترتيبها
            files = sorted(os.listdir(name))
            for file in files:
                if file.lower().endswith(IMAGE_EXTENSIONS):
                    # تشفير الاسم للتعامل مع المسافات واللغة العربية في الروابط
                    encoded_name = urllib.parse.quote(name)
                    encoded_file = urllib.parse.quote(file)
                    
                    # بناء الرابط النهائي
                    url = f"{GITHUB_BASE_URL}{encoded_name}/{encoded_file}"
                    image_urls.append(url)
            
            # 3. تحديث قائمة الصور لهذا الشخص
            person['images'] = image_urls
            print(f"تم تحديث: {name} بـ {len(image_urls)} صور")

    # 4. حفظ التغييرات في ملف جديد (للمراجعة) أو نفس الملف
    with open('reviews_updated.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print("\n✅ انتهى! الملف الجديد جاهز باسم: reviews_updated.json")

if __name__ == "__main__":
    update_reviews()