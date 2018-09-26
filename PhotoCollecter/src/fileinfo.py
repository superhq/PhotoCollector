#-*- coding:utf-8 -*-

from PIL import Image
from PIL.ExifTags import TAGS
img = Image.open(r"../resources/monkey.jpg")
exif_data = img._getexif()

if exif_data is not None:
    for k,v in exif_data.items():

        print(TAGS.get(k),'-----',v)