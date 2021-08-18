#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Ilya Savin Python Homework N16

# ------------------
# Написать программу, которая будет считывать из файла gps координаты,
# и формировать текстовое описание объекта и ссылку на google maps.
# ------------------


from geopy.geocoders import GoogleV3

coordinates = []
apk="AIzaSy" + "CYU5rG2aR" + "pxqBVSe51Et" +"JnmZdc" +"MG0pK" + str(chr(109)) + str(chr(119)) ### VERY DUMMY key protection
with open('coord.txt', 'r') as input_coord:  
    lines = input_coord.readlines()
    
    for i in range(len(lines) - 1):
        x, y = map(float, lines[i].split(', '))
        coordinates.append(((x, y)))
    input_coord.close()

    for x, y in coordinates:  
        geolocator = GoogleV3(api_key=apk)
        print("===================")
        print('coordinates: ', x, y)
        print('----------------', )
        print('Location: ', geolocator.reverse((x, y), language="ru",exactly_one=True))
        print(
            f'Google Maps URL: https://www.google.com/maps/search/?api={apk}&query={x},{y}')
