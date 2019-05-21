import pytesseract
from PIL import Image

image = Image.open('comparisons/stryfe.png')
string = pytesseract.image_to_string(image, lang="mff")
print(string)
