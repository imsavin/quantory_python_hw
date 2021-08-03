#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N9

# -------
# An irrational decimal fraction is created by concatenating the positive integers:
# 0.12345678910*1*112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
# ------------------


proizv = 1
for i in range(0, 7):
    proizv *= int("".join([str(j) for j in range(1, 1000000)])[10**i-1])
print(proizv)
