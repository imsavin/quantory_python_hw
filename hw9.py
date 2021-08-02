#!/usr/bin/python3
# Savin Ilya Python Homework N9

# 6 Problem
# The sum of the squares of the first ten natural numbers is,
# The square of the sum of the first ten natural numbers is,
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def summ_of_squares(nmbr):
    summ = 0
    for i in range(1, nmbr+1):
        summ += i**2
    return summ


def square_summ(nmbr):
    summ = 0
    for i in range(1, nmbr+1):
        summ += i
    return summ**2


diff_list = [square_summ(i) - summ_of_squares(i) for i in range(1, 101)]

print(diff_list)

# --------------------------------
