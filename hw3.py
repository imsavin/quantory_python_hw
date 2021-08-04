#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N3

# -------
# 1. После запуска предлагает пользователю ввести текст.
# 2. В качестве ответа печатает наиболее часто встречающееся в тексте слово
# или несколько таких слов, если имеет место "ничья". Также указывая
# сколько именно раз слово встретилось в тексте. (Игнорируйте заглавные буквы
# при отождествлении слов - то есть считайте слова "Подлодка" и "подлодка"
# одинаковыми, а разные формы слов - разными словами)
# После чего ждет следующего ввода.
# --------

from collections import Counter

while True:
    input_line = input("Enter string: ")
    input_list = input_line.lower().split()
    dict_counter = Counter(input_list)
    max_count = max(dict_counter.values())
    for k, v in dict_counter.items():
        if v == max_count:
            print(str(v) + " - " + k)
