#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Ilya Savin Python Homework N13

# ------------------
# Напишите функцию, которая переводит значения показаний
# температуры из Цельсия в Фаренгейт и наоборот.
# ------------------


def convert_temperature(value, convert_to='F'):
    if convert_to.upper() == 'F':
        return (value*1.8 + 32)
    elif convert_to.upper() == 'C':
        return (value - 32)/1.8
