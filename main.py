import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
import tensorflow as tf
import numpy as np
from labels import LABELS
from utils import preprocess_image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===== Load toàn bộ model .keras từ thư mục model/ =====
MODEL_DIR = "model"
models = []

for fname in os.listdir(MODEL_DIR):
    if fname.endswith(".keras"):
        model_path = os.path.join(MODEL_DIR, fname)
        print(f"[LOAD MODEL] {model_path}")
        models.append(tf.keras.models.load_model(model_path))

if not models:
    raise RuntimeError("[EMPTY MODEL]/")

print(f"[TOTAL MODELS LOADED]: {len(models)}")


@app.post("/predict")
async def predict(file: UploadFile = File(...)) -> Dict[str, List[str]]:
    image = preprocess_image(file.file)

    # Dự đoán với tất cả model và trung bình kết quả
    predictions = [model.predict(image, verbose=0)[0] for model in models]
    avg_prediction = np.mean(predictions, axis=0)

    # Ngưỡng gán nhãn
    threshold = 0.5
    predicted_labels = [LABELS[i] for i, prob in enumerate(avg_prediction) if prob >= threshold]

    if not predicted_labels:
        predicted_labels = [LABELS[np.argmax(avg_prediction)]]

    return {"predicted_labels": predicted_labels}
