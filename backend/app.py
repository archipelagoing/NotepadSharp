from flask import Flask, request, jsonify
import tempfile
from ocr import extract_text
from format_md import format_markdown

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_file():
    """Handle image uploads and return OCR-extracted Markdown."""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    file.save(temp_file.name)

    # Run OCR
    extracted_text = extract_text(temp_file.name)
    
    # Convert to Markdown
    markdown_text = format_markdown(extracted_text)

    return jsonify({"markdown": markdown_text})

if __name__ == "__main__":
    app.run(debug=True)
