#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N11

# -------
# Напишите функцию letters_range, которая ведет себя
# похожим на range образом, однако в качестве start и
# stop принимает не числа, а буквы латинского алфавита
# (в качестве step принимает целое число) и возращает
# не перечисление чисел, а список букв, начиная с
# указанной в качестве start, до указанной в качестве
# stop с шагом step (по умолчанию равным 1).
# -----


def letters_range(first_letter, second_letter, step=1):
    letters_list = []
    if all(i in range(ord('a'), ord('z')+1) for i in (ord(first_letter), ord(second_letter))):
        for i in range(ord(first_letter), ord(second_letter), step):
            letters_list.append(chr(i))
    return letters_list
