import pyautogui
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open("8b5a5ac1-f5fa-4aaf-9cb3-dd558acfa0d0.png")
output = pytesseract.image_to_string(img)

print(output)