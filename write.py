import os
import csv
import re

os.makedirs("module", exist_ok=True)

def save_image_filenames_to_csv(dataset_dir, output_csv):
    image_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
    lines = []

    # Regex để tách label và số thứ tự trong tên file
    pattern = re.compile(r"^(.*?)_(\d+)\.[^.]+$")  # ví dụ: chair_1.jpg

    # Duyệt files trong folder dataset (không đệ quy)
    for file in os.listdir(dataset_dir):
        if file.lower().endswith(image_extensions):
            match = pattern.match(file)
            if match:
                label_name = match.group(1)  # phần trước dấu _
                number = match.group(2)      # số thứ tự
                line = f"{file}: {label_name}"  # Giữ nguyên tên file có đuôi
                lines.append(line)
            else:
                print(f"[WARN] File tên không đúng định dạng: {file}")

    # Ghi vào CSV
    with open(output_csv, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for line in lines:
            writer.writerow([line])

    print(f"[SAVE] {len(lines)} [INTO] {output_csv}")

# Gọi hàm
save_image_filenames_to_csv("dataset", "module/pre_dataset.csv")
