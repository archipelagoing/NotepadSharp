from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import pytesseract
import numpy as np
from markdownify import markdownify

app = Flask(__name__)
CORS(app)  # Allow frontend requests

def preprocess_image(image):
    """Convert image to grayscale & apply thresholding."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh

def extract_text(image):
    """Extract text using Tesseract OCR."""
    processed_img = preprocess_image(image)
    text = pytesseract.image_to_string(processed_img)
    return text

def convert_to_markdown(text):
    """Convert structured text to Markdown format."""
    markdown = []
    for line in text.split("\n"):
        line = line.strip()
        if line.isupper():
            markdown.append(f"# {line}")  # Convert to heading
        elif line.startswith("-") or line.startswith("*"):
            markdown.append(line)  # Preserve bullet points
        elif ":" in line and not line.endswith(":"):
            markdown.append(f"**{line}**")  # Bold key-value pairs
        else:
            markdown.append(line)
    return "\n".join(markdown)

@app.route("/upload", methods=["POST"])
def upload_image():
    file = request.files["image"]
    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    extracted_text = extract_text(img)
    markdown_text = convert_to_markdown(extracted_text)

    return jsonify({"markdown": markdown_text})

if __name__ == "__main__":
    app.run(debug=True)
