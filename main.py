from PIL import Image


# ファイルの縦横比を調べる
with Image.open('shoutingChickenIconBlackLine2.jpg') as im:
    width, height = im.size
    print(width)
    print(height)
