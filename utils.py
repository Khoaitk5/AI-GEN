from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from typing import BinaryIO
import io
from datetime import datetime
import socket

def preprocess_image(file: BinaryIO):
    file.seek(0)
    img_bytes = file.read()              # đọc nội dung file thành bytes
    bytes_io = io.BytesIO(img_bytes)     # tạo đối tượng BytesIO từ bytes
    image = load_img(bytes_io, target_size=(224, 224))
    image = img_to_array(image) / 255.0
    return np.expand_dims(image, axis=0)


def get_name():
    hostname = socket.gethostname()  # Lấy tên máy (ví dụ: DESKTOP-123ABC)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{hostname}-{timestamp}"
