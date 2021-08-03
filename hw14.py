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


class Employee:

    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def printinfo(self):
        print("====Employee Info====")
        print("Name: ", self.__name)
        print("Position: ", self.__position)
        print("Salary: ", self.__salary)


Mary = Employee("Mary Doe", "Technician Director", 100000)

with open('pickle_exchange.pkl', 'wb') as outfile:
    pickle.dump(Mary, outfile)
