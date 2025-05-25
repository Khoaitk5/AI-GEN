import requests
import json

def predict_image(url: str, image_path: str):
    with open(image_path, "rb") as f:
        files = {"file": (image_path, f, "image/jpeg")}
        response = requests.post(url, files=files)

    print("Status code:", response.status_code)

    try:
        data = response.json()  # Parse JSON response thành dict
        # In đẹp JSON ra console
        print("Response JSON:")
        print(json.dumps(data, indent=2, ensure_ascii=False))

        predicted_labels = data.get("predicted_labels", [])
        print("[PREDICTED LABELS]:")
        for label in predicted_labels:
            print(" -", label)

        return data  # Trả về dict JSON

    except Exception as e:
        print("[ERROR]:", e)
        return None

if __name__ == "__main__":
    url = "http://127.0.0.1:8000/predict"
    image_path = "demo_image.jpg"  # Thay bằng ảnh thật của bạn
    result_json = predict_image(url, image_path)
