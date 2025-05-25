from icrawler.builtin import GoogleImageCrawler
from labels import LABELS
import os
import shutil
import random

if os.path.exists("dataset"):
    shutil.rmtree("dataset")
os.makedirs("dataset", exist_ok=True)

number_of_each = 2  # số lượng data cho từng label

# Danh sách suffixes đa dạng, không liên quan tutorial
suffixes = [
    "", " diy ideas", " project", " craft", " handmade", " design", 
    " art", " creative", " model", " decoration", " hack", " inspiration"
]

for label in LABELS:
    if not label.strip():
        continue

    # Chọn ngẫu nhiên 1 suffix mỗi lần chạy
    suffix = random.choice(suffixes)
    keyword = f"diy {label}{suffix}"
    print(f"[Starting]: {keyword}")

    # Tạo thư mục tạm để crawl ảnh
    temp_dir = os.path.join("temp", label)
    os.makedirs(temp_dir, exist_ok=True)

    google_crawler = GoogleImageCrawler(storage={'root_dir': temp_dir})
    google_crawler.crawl(keyword=keyword, max_num=number_of_each)

    # Lấy danh sách file trong thư mục tạm
    files = os.listdir(temp_dir)
    for i, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1].lower()
        old_path = os.path.join(temp_dir, filename)
        new_filename = f"{label}_{i}{ext}"
        new_path = os.path.join("dataset", new_filename)

        # Di chuyển và đổi tên file về thư mục dataset
        shutil.move(old_path, new_path)
    # Xóa thư mục tạm đã dùng
    shutil.rmtree(temp_dir)

    print(f"[Finished]: {label}\n")

if os.path.exists("temp"):
    shutil.rmtree("temp")
