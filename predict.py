import requests

url = "http://127.0.0.1:8000/predict"
image_path = "demo_image.jpg"  # Thay bằng đường dẫn ảnh thật của bạn

with open(image_path, "rb") as f:
    files = {"file": (image_path, f, "image/jpeg")}
    response = requests.post(url, files=files)

print("Status code:", response.status_code)
print("Response text:", response.text)

try:
    data = response.json()
    # Giả sử data có dạng: {"predicted_labels": ["label1", "label2", ...]}
    predicted_labels = data.get("predicted_labels", [])
    print("[PREDICTED LABELS]:")
    for label in predicted_labels:
        print(" -", label)
except Exception as e:
    print("[ERROR]:", e)
