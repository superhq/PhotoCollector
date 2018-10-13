# -*- coding:utf-8 -*-

from PIL import Image
from PIL.ExifTags import TAGS
from PyQt5.QtMultimedia import QMediaPlayer,QMediaMetaData,QMediaContent
from PyQt5.QtCore import QUrl
import os




class PhotoInfo:
    def getinfo(self, path):
        datetime = None
        maker = None
        suffix = os.path.splitext(path)[-1].lower()
        try:
            with Image.open(path) as img:
                exif_data = img._getexif()
                if exif_data:
                    for k, v in exif_data.items():
                        # print(TAGS.get(k),v)
                        if TAGS.get(k) == 'DateTimeOriginal':
                            datetime = v
                        if TAGS.get(k) == 'Make':
                            maker = v
        except Exception as e:
            print(e)
        return (datetime,maker,suffix)

# import cv2
# vid = cv2.VideoCapture(r'‪C:\Users\Qun\Desktop\video.mov')
# height = vid.get(cv2) # always 0 in Linux python3
# width  = vid.get(cv2.CAP_PROP_FRAME_WIDTH)  # always 0 in Linux python3
# print ("opencv: height:{} width:{}".format( height, width))

# from exifread import process_file
#
# with open(r'E:\huawei-20151212\VID_20151201_205840.mp4','rb') as f:
#     tags = process_file(f)
#     print(tags)
