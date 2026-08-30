from PIL import Image
import pytesseract

# Windows Only: You must point pytesseract directly to your installed engine executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_tesseract(image_path):
    try:
        # Open the image using Pillow (PIL)
        img = Image.open(image_path)
        
        # Optional: Convert to grayscale ('L') to improve OCR accuracy
        img_gray = img.convert("L")
        
        # Extract text from the image
        extracted_text = pytesseract.image_to_string(img_gray)
        
        return extracted_text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Usage
text = extract_text_tesseract("sample_document.jpg")
print(text)
