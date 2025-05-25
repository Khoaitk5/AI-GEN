import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
import tensorflow as tf
import numpy as np
from labels import LABELS
from utils import preprocess_image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Có thể sửa thành domain cụ thể khi deploy
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_DIR = "model"
models = []

def load_models(model_dir: str) -> List[tf.keras.Model]:
    loaded_models = []
    for fname in os.listdir(model_dir):
        if fname.endswith(".keras"):
            model_path = os.path.join(model_dir, fname)
            print(f"[LOAD MODEL] {model_path}")
            model = tf.keras.models.load_model(model_path)
            loaded_models.append(model)
    if not loaded_models:
        raise RuntimeError("[EMPTY MODEL] No .keras models found in model directory")
    print(f"[TOTAL MODELS LOADED]: {len(loaded_models)}")
    return loaded_models

# Load models once at startup
models = load_models(MODEL_DIR)

@app.post("/predict")
async def predict(file: UploadFile = File(...)) -> Dict[str, List[str]]:
    try:
        # Preprocess image file stream
        image = preprocess_image(file.file)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image file: {e}")

    # Ensemble prediction: trung bình xác suất từ tất cả model
    predictions = [model.predict(image, verbose=0)[0] for model in models]
    avg_prediction = np.mean(predictions, axis=0)

    # Ngưỡng gán nhãn (threshold)
    threshold = 0.5
    predicted_labels = [LABELS[i] for i, prob in enumerate(avg_prediction) if prob >= threshold]

    # Nếu không có nhãn nào đạt threshold, lấy nhãn có xác suất cao nhất
    if not predicted_labels:
        max_index = np.argmax(avg_prediction)
        predicted_labels = [LABELS[max_index]]

    return {"predicted_labels": predicted_labels}
