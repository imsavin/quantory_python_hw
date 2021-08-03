#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Savin Ilya Python Homework N12

# ------------
# Написать функцию Фиббоначи fib(n), которая вычисляет
# элементы последовательности Фиббоначи:
# 1 1 2 3 5 8 13 21 34 55 .......
# ------------


def fib(n):
    fib_1 = fib_2 = 1
    while n > 0:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        n -= 1
    return(fib_2)


fib_nmbr = int(input("Enter number of Fibonacci sequence element: "))
print(fib(fib_nmbr))
