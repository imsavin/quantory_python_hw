#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N9

# ----------
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c***2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# ----------

answer_list = [a * b * c for a in range(1, 500) for b in range(a, 500)
               for c in range(b, 500) if ((a**2 + b**2 == c**2) and (a + b + c == 1000))]
print(answer_list)
