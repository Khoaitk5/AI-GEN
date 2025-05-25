from PIL import Image

try:
    img = Image.open("demo_image.jpg")
    img.verify()  # kiểm tra xem ảnh có lỗi không
    print("[VALID]")
except Exception as e:
    print("[INVALID]:", e)