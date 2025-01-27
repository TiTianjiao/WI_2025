from PIL import Image
print("Pillow is installed and working!")



# Location of the image
img = Image.open("30617756_cellviability.png")

img.show()
# size of the image
print(img.size)

# format of the image
print(img.format)
print(img.mode) #RGB, 3×8-bit pixels, true color



# Open the image
img = Image.open("30617756_cellviability.png")


# Extract text from the image
text = pytesseract.image_to_string(img)
print(text)


import easyocr
reader = easyocr.Reader(['en'])  # Initialize for English
result = reader.readtext("30617756_cellviability.png")
print(result)

import cv2
import pytesseract

# Read and preprocess the image
img = cv2.imread("30617756_cellviability.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)
print(text)

from paddleocr import PaddleOCR


ocr = PaddleOCR(use_angle_cls=True)  # Initialize OCR model
result = ocr.ocr("example_image.png", cls=True)
print(result)


