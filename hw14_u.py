#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N14

# ---------------
# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.
# ---------------

import pickle
from hw14 import Employee

with open('pickle_exchange.pkl', 'rb') as infile:
    Mary = pickle.load(infile)

Mary.printinfo()
