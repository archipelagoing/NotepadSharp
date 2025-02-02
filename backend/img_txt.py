from PIL import Image
from transformers import TrOCRProcessor
from transformers import VisionEncoderDecoderModel
import sys

# takes an image path as an argument(s) (other arguments are irrelevant)
args = []
for line in sys.stdin:
    line.rstrip()
    args.append(line)

# defailt image
if (len(args) == 0):
  args.append("pee.jpg")

image = Image.open(args[0]).convert("RGB")

# model & processor loaded from different script
pixel_values = processor(image, return_tensors="pt").pixel_values

# generate ids and text
generated_ids = model.generate(pixel_values)
generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(generated_text)
