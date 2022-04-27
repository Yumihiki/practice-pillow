from PIL import Image
import glob
import os

# ファイルの縦横比を調べる
with Image.open('shoutingChickenIconBlackLine2.jpg') as im:
    width, height = im.size
    print(width)
    print(height)

# 角度を変化させる
with Image.open('shoutingChickenIconBlackLine2.jpg') as im2:
    im2.rotate(45).show()
