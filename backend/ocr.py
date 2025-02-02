from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image

# Load TrOCR model
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

def extract_text(image_path):
    """Extract handwritten text from an image using TrOCR."""
    image = Image.open(image_path).convert("RGB")
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    return processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

# Example usage
if __name__ == "__main__":
    text = extract_text("data/sample_handwriting.jpg")
    print("Extracted Text:", text)
