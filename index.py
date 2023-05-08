import pytesseract
from PIL import Image

# Carga la imagen
image = Image.open('images/descarga.jpg')
text = pytesseract.image_to_string(image)
# Realiza la conversión OCR
print(text)