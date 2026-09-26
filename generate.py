import os
import requests
import json
import time

def read_prompts():
    if not os.path.exists('prompts.txt'):
        print("❌ لم يتم العثور على ملف prompts.txt")
        return []
    with open('prompts.txt', 'r', encoding='utf-8') as f:
        prompts = [line.strip() for line in f if line.strip()]
    return prompts

def main():
    prompts = read_prompts()
    print(f"🎯 تم العثور على {len(prompts)} وصف للتوليد.")
    
    os.makedirs('outputs', exist_ok=True)
    
    hailuo_api_key = os.getenv('HAILUO_API_TOKEN')
    
    for idx, prompt in enumerate(prompts, start=1):
        print(f"\n🎬 [{idx}/{len(prompts)}] جاري معالجة الوصف: {prompt}")
        output_filename = f"outputs/video_{idx}.mp4"
        
        if hailuo_api_key:
            headers = {"Authorization": f"Bearer {hailuo_api_key}", "Content-Type": "application/json"}
            payload = {"prompt": prompt}
            try:
                res = requests.post("https://api.acedatacloud.com/hailuo/generate", json=payload, headers=headers)
                print(f"✅ تم إرسال الطلب لـ Hailuo API بنجاح.")
            except Exception as e:
                print(f"❌ خطأ أثناء الاتصال بـ API: {e}")
        else:
            print("⚠️ لم يتم العثور على مفتاح Hailuo API Token، سيتم تنفيذ سكريبت التجهيز والاختبار.")

if __name__ == "__main__":
    main()
