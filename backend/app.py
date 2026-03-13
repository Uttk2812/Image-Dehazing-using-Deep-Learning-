from flask import Flask, render_template, request, jsonify
import base64
import cv2

from inference import dehaze_image

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dehaze", methods=["POST"])
def dehaze():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]

    try:
        output_img = dehaze_image(file)

        # Encode image to PNG
        _, buffer = cv2.imencode(".png", output_img)
        image_base64 = base64.b64encode(buffer).decode("utf-8")

        return jsonify({"image": image_base64})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": "Processing failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)
