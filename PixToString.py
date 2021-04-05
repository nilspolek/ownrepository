import pytesseract as tess
from PIL import Image

img = Image.open("./iCloud_Photos/IMG_2838.JPEG")
text = tess.image_to_string(img)