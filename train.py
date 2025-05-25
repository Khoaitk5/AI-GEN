import os
import csv
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split
from labels import LABELS
import utils

# Cấu hình
FILE_NAME = utils.get_name();
CSV_PATH = "module/pro_dataset.csv"
IMAGE_DIR = "dataset"
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 10

def load_data_from_csv(csv_path):
    image_paths = []
    labels = []

    with open(csv_path, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)  # bỏ dòng tiêu đề

        for row in reader:
            filename = row[0].strip()
            label_vector = list(map(int, row[1:]))
            full_image_path = os.path.join(IMAGE_DIR, filename)

            if os.path.exists(full_image_path):
                image_paths.append(full_image_path)
                labels.append(label_vector)

    return np.array(image_paths), np.array(labels, dtype=np.float32)

def preprocess_image(path):
    img = load_img(path, target_size=IMAGE_SIZE)
    img_array = img_to_array(img) / 255.0
    return img_array

def build_dataset(X, y):
    images = np.array([preprocess_image(p) for p in X])
    return tf.data.Dataset.from_tensor_slices((images, y)).shuffle(len(X)).batch(BATCH_SIZE)

def build_model(output_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(224, 224, 3)),
        tf.keras.layers.Conv2D(32, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(64, 3, activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(output_dim, activation='sigmoid')  # multi-label
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model

def train_model_from_csv():
    print("[LOAD DATA]")
    X, y = load_data_from_csv(CSV_PATH)

    print("[SET UP DATA]")
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    print("[CREATE TENSORFLOW DATA]")
    train_ds = build_dataset(X_train, y_train)
    val_ds = build_dataset(X_val, y_val)

    print("[BUILDING MODEL]")
    model = build_model(len(LABELS))

    print("[START TRAINNING]")
    model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS)

    os.makedirs("model", exist_ok=True)
    model.save(f"model/{FILE_NAME}.keras")
    print(f"[DONE] model/{FILE_NAME}.keras")

# Gọi hàm
if __name__ == "__main__":
    train_model_from_csv()
    
# Đổi tên
os.rename("module/pre_dataset.csv", f"module/pre_{FILE_NAME}.csv")
os.rename("module/pro_dataset.csv", f"module/pro_{FILE_NAME}.csv")
