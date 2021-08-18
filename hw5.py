#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N5

# -------
# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода ввиде строки (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:

# 1. После запуска предлагает пользователю ввести неотрицательные целые числа,
# разделенные через пробел и ожидает ввода от пользователя.
# 2. Находит наименьшее положительное число, не входящее в данный пользователем
# список чисел и печатает его.
# --------

input_string = input("Enter string of numbers: ")
numbers_list = []
split_string = input_string.split()
for i in split_string:
    numbers_list.append(int(i))

numbers_list = list(set(numbers_list))  
numbers_list.sort()

counter = 0
flag = 0
for i in numbers_list:
    counter += 1
    if i > counter:
        print(counter)
        flag = 1
        break

if flag == 0:
    print(counter+1)
