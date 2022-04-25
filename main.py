from PIL import Image


image = Image.open('画像名')
width, height = image.size
print(width)
print(height)
