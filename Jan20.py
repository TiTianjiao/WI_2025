# Import required libraries
from PIL import Image
import pytesseract
import easyocr
import cv2
from paddleocr import PaddleOCR

# File path
image_path = "30617756_cellviability.png"

# Check if the file exists
try:
    # Open the image using PIL
    img = Image.open(image_path)

    # Display the image properties
    print(f"Image Size: {img.size}")
    print(f"Image Format: {img.format}")
    print(f"Image Mode: {img.mode}")  # RGB, etc.

    # Display the image
    img.show()

    # Extract text using pytesseract
    print("\n--- Using pytesseract ---")
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Adjust the path if needed
    text = pytesseract.image_to_string(img)
    print("Extracted Text:\n", text)

    # Extract text using easyocr
    print("\n--- Using easyocr ---")
    reader = easyocr.Reader(['en'])  # Initialize for English
    result = reader.readtext(image_path)
    print("EasyOCR Results:\n", result)

    # Extract text using OpenCV and pytesseract
    print("\n--- Using OpenCV + pytesseract ---")
    img_cv = cv2.imread(image_path)
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    cv_text = pytesseract.image_to_string(gray)
    print("Extracted Text (OpenCV):\n", cv_text)

    # Extract text using PaddleOCR
    print("\n--- Using PaddleOCR ---")
    ocr = PaddleOCR(use_angle_cls=True)  # Initialize OCR model
    paddle_result = ocr.ocr(image_path, cls=True)
    print("PaddleOCR Results:\n", paddle_result)

except FileNotFoundError:
    print(f"Error: File '{image_path}' not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")
