from ultralytics import YOLO
import numpy as np
from PIL import Image
import io
import base64
import time

# 226ms pytorch
# 192.0ms onnx
# tensorRt


def YoloV8():
    # 모델 불러오기
    model = YOLO(
        "C:\\Users\\minsu\\Documents\\ocearn\\Django_chat\\backend\ocean\\ai\\best.onnx")
    start_time = time.time()
    # 이미지 추론
    res = model(
        "C:\\Users\\minsu\\Documents\\ocearn\\Django_chat\\backend\ocean\\ai\\test_img.jpg")
    end_time = time.time()
    # 넘파이 배열로 변환
    arr = np.array((res[0].plot()))
    inference_time = end_time - start_time
    image = Image.fromarray(arr)
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    print(inference_time)
    return img_str
