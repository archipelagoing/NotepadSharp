# dependent on transformers which can be installed by
# pip install -q transformers
from transformers import TrOCRProcessor
from transformers import VisionEncoderDecoderModel
processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")
