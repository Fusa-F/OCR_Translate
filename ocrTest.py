from PIL import Image
import pytesseract

from googletrans import Translator
import sys

import io 
import urllib.request

# import sys
import os

imgA = Image.open("Eng1C_01.png")
txt = pytesseract.image_to_string(imgA, lang="eng")
print(txt)
print(Translator().translate(txt, src = 'en' ,dest = 'ja').text)

imgB = Image.open("Eng1C_02.png")
txt = pytesseract.image_to_string(imgB, lang="eng")
print(txt)
print(Translator().translate(txt, src = 'en' ,dest = 'ja').text)

# # 画像のURL 今回はPythonのロゴを使用
# url = "https://www.python.org/static/img/python-logo@2x.png"
# # 画像データを取得する
# img_in = urllib.request.urlopen(url).read()
# img_bin = io.BytesIO(img_in)
# # Pillowで開き、画像を保存する
# img = Image.open(img_bin)
# print(pytesseract.image_to_string(img, lang="jpn"))