#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N8

# ----------
# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода в виде строки (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:
# 1. После запуска предлагает пользователю ввести текст.
# 2. Проверяет и, если возможно, преобразовывает полученный текст в число,
# используя рекурсивную функцию.
# Если число четное - делит его на 2 и выводит результат.
# Если число нечетное - умножает на 3 и прибавляет 1.
# После чего ждет следующего ввода.
# 3.При получении в качестве вводных данных 'cancel' завершает свою работу.
# -------------


def recursive_func(input_str, order, number):
    try:
        number = number + int(input_str[-1:])*(10**order)
        order = order + 1
        if len(input_str) == 1:
            return number
        else:
            return recursive_func(input_str[:len(input_str)-1],order,number)
    except ValueError:
        print("Cant convert to stirng")

        

while True:
    input_str = input("Enter number: ")
    if input_str == "cancel":
        print("Bye!")
        break
    number = recursive_func(input_str,0,0)
    if number % 2 == 0:
        print(int(number / 2))
    else:
        print(number*3 - 1)
