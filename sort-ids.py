import json
from datetime import datetime

def sort_reviews(input_file, output_file):
    try:
        # 1. تحميل البيانات من ملف JSON
        with open(input_file, 'r', encoding='utf-8') as f:
            reviews = json.load(f)

        # 2. ترتيب التقييمات بناءً على التاريخ
        # نستخدم datetime.strptime للتأكد من أن الترتيب زمني وليس نصي
        reviews.sort(key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))

        # 3. إعادة تعيين المعرفات (ID) لتبدأ من 1 للأقدم
        for index, review in enumerate(reviews, start=1):
            review['id'] = index

        # 4. حفظ البيانات المحدثة في ملف جديد
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(reviews, f, ensure_ascii=False, indent=4)
        
        print(f"✅ تمت العملية بنجاح! تم حفظ الملف المحدث باسم: {output_file}")

    except Exception as e:
        print(f"❌ حدث خطأ: {e}")

import os
print("تجد الملف هنا بالضبط:")
print(os.path.abspath('reviews_sorted_final.json'))