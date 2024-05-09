import pandas as pd
import cv2
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_list = ['1회차.png','teset03.png','모바일CPU벤치.jpg']

result = []
for image in image_list:
    text = pytesseract.image_to_string(image)
    result.append(text)
    print(text)
    print()

#print(result)

