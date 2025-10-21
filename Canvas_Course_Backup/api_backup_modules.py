import os, requests, re
from bs4 import BeautifulSoup
from tqdm import tqdm

# ======== 👇 在这里填写你的信息 👇 ========
API_URL = "https://jhu.instructure.com/api/v1"
TOKEN = ""
OUTPUT_DIR = "canvas_web_backup"
# ==========================================


headers = {"Authorization": f"Bearer {TOKEN}"}
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Step 1. 获取所有课程
courses = requests.get(f"{API_URL}/courses?per_page=100", headers=headers).json()

for course in courses:
    cid = course.get("id")
    cname = course.get("name", f"course_{cid}").replace("/", "_").strip()
    print(f"\n📘 {cname} (ID: {cid})")
    course_dir = os.path.join(OUTPUT_DIR, cname)
    os.makedirs(course_dir, exist_ok=True)

    # Step 2. 获取课程的所有 modules
    modules = requests.get(f"{API_URL}/courses/{cid}/modules?per_page=100", headers=headers).json()
    if not isinstance(modules, list) or not modules:
        print("⚠️  No modules found or access restricted.")
        continue

    for m in tqdm(modules, desc=f"Scanning modules for {cname}"):
        mid = m["id"]
        items = requests.get(f"{API_URL}/courses/{cid}/modules/{mid}/items?per_page=100", headers=headers).json()
        for item in items:
            if item.get("type") == "File":
                file_id = item["content_id"]
                # 获取文件信息
                file_info = requests.get(f"{API_URL}/files/{file_id}", headers=headers).json()
                fname = file_info["display_name"]
                furl = file_info["url"]
                try:
                    r = requests.get(furl)
                    with open(os.path.join(course_dir, fname), "wb") as f:
                        f.write(r.content)
                except Exception as e:
                    print(f"❌ Error downloading {fname}: {e}")

print("\n✅ All module files downloaded.")
print(f"Files saved in: {os.path.abspath(OUTPUT_DIR)}")
