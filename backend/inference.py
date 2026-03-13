import cv2
import numpy as np

def dehaze_image(file):
    # Read raw bytes from uploaded file
    file_bytes = np.frombuffer(file.read(), np.uint8)

    # Decode image using OpenCV
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # ✅ SAFETY CHECK
    if image is None:
        raise ValueError("Invalid image file")

    # Simple enhancement (placeholder for Phase-1)
    enhanced = cv2.detailEnhance(image, sigma_s=12, sigma_r=0.15)

    return enhanced
