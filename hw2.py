#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N2

# -----
# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода в виде строк (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:

# 1. После запуска предлагает пользователю ввести текст, содержащий любые слова,
# слоги, числа или их комбинации, разделенные пробелом.
# 2. Считывает строку с текстом, и разбивает его на элементы списка, считая
# пробел символом разделителя.
# 3. Печатает этот же список элементов (через пробел), однако с удаленными
# дубликатами.
# -------

input_line = input("Enter string: ")
print(set(input_line.split())
