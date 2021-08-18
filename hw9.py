#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N9

# 6 Problem
# The sum of the squares of the first ten natural numbers is,
# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

print((sum([sq_of_sum for sq_of_sum in range(1, 101)])**2) -  (sum([sum_of_sq**2 for sum_of_sq in range(1, 101)])))
# --------------------------------
