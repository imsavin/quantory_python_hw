#!/usr/bin/python3
# Savin Ilya Python Homework N6

# ----------
# The decimal number, 585 = 1001001001 in binary, is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in
# base 10 and base 2. (Please note that the palindromic number,
# in either base, may not include leading zeros.)

# Напишите программу, которая решает описанную выше задачу и печатает ответ.
# -----------


def ispalindromic(s):
    reversed_string = s[::-1]
    return s == reversed_string


summ = 0
for i in range(1, 1000000):
    if ispalindromic(str(i)) and ispalindromic("{0:b}".format(i)):
        summ += i

print(summ)
