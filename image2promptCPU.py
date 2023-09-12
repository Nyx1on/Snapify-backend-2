import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

img_url = 'http://127.0.0.1:8000/uploads/2f24de8e5ea7a30948933767f8437f33.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

# conditional image captioning
text = "a photography of"
inputs = processor(raw_image, text, return_tensors="pt")

out = model.generate(**inputs)
print(processor.decode(out[0], skip_special_tokens=True))
# >>> a photography of a woman and her dog

# unconditional image captioning
# inputs = processor(raw_image, return_tensors="pt")

# out = model.generate(**inputs)
# print(processor.decode(out[0], skip_special_tokens=True))


def generateCaption(img_urls):
    captions = []
    
    for img_url in img_urls:
        raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

        inputs = processor(raw_image, return_tensors="pt")

        out = model.generate(**inputs)

        caption = processor.decode(out[0], skip_special_tokens=True)

        captions.append(caption)

    return captions
