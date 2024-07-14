import os, sys
from PIL import Image

#create image folder var
img_file = os.getcwd()

#create sive var
size = (800,600)

#loop through image folder
count = 10
for filename in os.listdir(img_file):
    
#open image
    if filename.lower().endswith((".jpg")):
        with Image.open(os.path.join(img_file, filename)) as img:
#resize image
            img_resized = img.resize(size, Image.LANCZOS)
#save image
            img_resized.save(os.path.join(img_file, f"sp{count}.jpg"))
            count += 1