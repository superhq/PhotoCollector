# -*- coding:utf-8 -*-

from PIL import Image
from PIL.ExifTags import TAGS

# img = Image.open(r"E:\huawei-20151212\VID_20151201_205840.mp4")
# exif_data = img._getexif()
#
# if exif_data is not None:
#     for k, v in exif_data.items():
#         print(TAGS.get(k), '-----', v)


class FileInfo:
    def getinfo(self, path):
        datetime = None
        maker = None
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
        return (datetime,maker)

# from exifread import process_file
#
# with open(r'E:\huawei-20151212\VID_20151201_205840.mp4','rb') as f:
#     tags = process_file(f)
#     print(tags)
