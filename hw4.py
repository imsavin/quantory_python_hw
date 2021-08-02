#!/usr/bin/python3
# Savin Ilya Python Homework N4

# -----------
# Встроенная функция input позволяет ожидать и возвращать данные из стандартного
# ввода ввиде строк (весь введенный пользователем текст до нажатия им enter).
# Используя данную функцию, напишите программу, которая:

# 1. После запуска предлагает пользователю ввести целые неотрицательные числа,
# разделенные любым не цифровым литералом (пробел, запятая, %, буква и т.д.).
# 2. Получив вводные данные, выделяет полученные числа, суммирует их,
# и печатает полученную сумму.
# -----------

input_string = input("Enter text: ")
temp_str = input_string
numbers_counter = 0
numbers_string = ""
for i in range(0, len(temp_str)):
    if temp_str[i].isnumeric():
        if i > 0 and temp_str[i-1] == "-":
            numbers_string = numbers_string + "-" + temp_str[i]
        else:
            numbers_string = numbers_string + temp_str[i]
    else:
        numbers_string = numbers_string + " "

summ = 0
for i in numbers_string.split():
    summ = summ + int(i)

print(summ)
