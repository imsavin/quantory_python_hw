#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Ilya Savin Python Homework N17

# ------------------
# Написать скрипт, который будет вытаскивать gps данные
# из фотографии (jpg файл) и передавать их на вход программе
# из hw16.txt
# ------------------


from geopy.geocoders import GoogleV3
import os
from PIL import Image
from PIL.ExifTags import TAGS,GPSTAGS


def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

def get_geotagging(exif):
    if not exif:
        raise ValueError("No EXIF metadata found")

    geotagging = {}
    for (idx, tag) in TAGS.items():
        if tag == 'GPSInfo':
            if idx not in exif:
                raise ValueError("No EXIF geotagging found")

            for (key, val) in GPSTAGS.items():
                if key in exif[idx]:
                    geotagging[val] = exif[idx][key]

    return geotagging

def get_decimal_from_dms(dms, ref):
    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0
    if ref in ['S', 'W']:
        degrees = -degrees
        minutes = -minutes
        seconds = -seconds

    return round(degrees + minutes + seconds, 5)

def get_coordinates(geotags):
    lat = get_decimal_from_dms(geotags['GPSLatitude'], geotags['GPSLatitudeRef'])

    lon = get_decimal_from_dms(geotags['GPSLongitude'], geotags['GPSLongitudeRef'])

    return (lat,lon)



coordinates = []
apk="AIzaSy" + "CYU5rG2aR" + "pxqBVSe51Et" +"JnmZdc" +"MG0pK" + str(chr(109)) + str(chr(119)) ### VERY DUMMY key protection

pic_dir = os.getcwd() + "/exifpic/"
imglist = os.listdir(pic_dir)
for imgfile in imglist:
   exif = get_exif(pic_dir + imgfile)
   geotags = get_geotagging(exif)
   geolocator = GoogleV3(api_key=apk)
   print("===================")
   print('coordinates: ', get_coordinates(geotags))
   print('----------------', )
   print('Location: ', geolocator.reverse(get_coordinates(geotags), language="ru",exactly_one=True))
