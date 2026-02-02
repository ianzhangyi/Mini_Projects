import os
import requests
from tqdm import tqdm

# ====== 👇 先在这里填写你的信息 👇 ======
API_URL = "https://jhu.instructure.com/api/v1"
TOKEN = "生成api"
OUTPUT_DIR = "canvas_backup"   # 下载保存的文件夹
# =======================================
print('Start to backup files from Canvas...')
headers = {"Authorization": f"Bearer {TOKEN}"}
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 获取所有课程
print("Fetching your Canvas courses...")
courses = requests.get(f"{API_URL}/courses?per_page=100", headers=headers).json()

for course in courses:
    cid = course.get("id")
    cname = course.get("name", "Unknown_Course").replace("/", "_").strip()
    course_dir = os.path.join(OUTPUT_DIR, cname)
    os.makedirs(course_dir, exist_ok=True)
    print(f"\n📚 课程：{cname}")


    page = 1
    while True:
        resp = requests.get(f"{API_URL}/courses/{cid}/files?per_page=100&page={page}", headers=headers)
        files = resp.json()
        if not files or not isinstance(files, list):
            break

        for f in tqdm(files, desc=f"Downloading files (page {page})"):
            fname = f.get("display_name", f"file_{f['id']}")
            furl = f.get("url")
            if not furl:
                continue
            try:
                r = requests.get(furl)
                with open(os.path.join(course_dir, fname), "wb") as out:
                    out.write(r.content)
            except Exception as e:
                print(f"❌ Error downloading {fname}: {e}")
        page += 1

print("\n✅ 所有课程文件已下载完成！")
print(f"文件保存路径：{os.path.abspath(OUTPUT_DIR)}")
