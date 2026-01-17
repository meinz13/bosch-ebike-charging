import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pandas as pd
import os

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
image_folder = r'/home/user/path/to/screenshots'
data = []

for filename in os.listdir(image_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
        image_path = os.path.join(image_folder, filename)
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        print(text)
        columns = text.split()
        data.append(columns)

pd.DataFrame(data).to_csv('output.csv', index=False)
